import os
import logging
import openai
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, CommandHandler, CallbackContext
import discord
from discord.ext import commands
import json
import subprocess  # Added for running the Launcher.py script
import sys  # Import sys for accessing the executable

# ANSI escape codes for colors
GREEN = "\033[92m"      # Green
BLUE = "\033[94m"       # Blue
RED = "\033[91m"        # Red
PINK = "\033[95m"       # Pink
RESET = "\033[0m"       # Reset color

# Load API keys and tokens from config.py
try:
    from config import api_key, telegram_token, discord_token
except ImportError:
    print("Error: Missing config.py with required keys.")
    api_key = telegram_token = discord_token = None

# Load identity from identity.txt
def load_identity():
    if os.path.exists("identity.txt"):
        with open("identity.txt", "r") as f:
            return f.read().strip()
    return "You are a friendly AI assistant."

identity_description = load_identity()
openai.api_key = api_key

# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load conversation history
def load_history():
    if os.path.exists("conversation.json"):
        with open("conversation.json", "r") as f:
            return json.load(f)
    return {}

def save_history(history):
    with open("conversation.json", "w") as f:
        json.dump(history, f)

# Chat function with OpenAI API
def chat_with_ai(prompt, user_id, history):
    # Combine identity with user prompt
    full_prompt = f"{identity_description}\nUser: {prompt}\nAI:"
    
    # Initialize user-specific history if it doesn't exist
    if user_id not in history:
        history[user_id] = [{"role": "system", "content": identity_description}]  # Add identity as system message

    # Add the user's message to the history
    history[user_id].append({"role": "user", "content": prompt})

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=history[user_id]
        )
        ai_response = response.choices[0].message.content.strip()

        # Add AI response to the history
        history[user_id].append({"role": "assistant", "content": ai_response})
        save_history(history)  # Save the updated history
        return ai_response
    except Exception as e:
        logger.error(f"Error communicating with OpenAI: {e}")
        return "Sorry, I couldn't process your request."

# Telegram bot functions
def run_telegram_bot():
    if not telegram_token:
        print("Telegram token is missing. Skipping Telegram bot.")
        return

    app = ApplicationBuilder().token(telegram_token).build()
    history = load_history()

    async def handle_message(update: Update, context: CallbackContext):
        user_message = update.message.text
        user_id = update.effective_user.id
        response = chat_with_ai(user_message, user_id, history)
        await update.message.reply_text(response)

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    async def reset_history(update: Update, context: CallbackContext):
        user_id = update.effective_user.id
        if user_id in history:
            del history[user_id]  # Clear user-specific history
            save_history(history)  # Save the updated history
            await update.message.reply_text("Your conversation history has been reset.")
        else:
            await update.message.reply_text("No conversation history found to reset.")

    app.add_handler(CommandHandler("reset", reset_history))

    print("Telegram bot is running. Press Ctrl+C to stop.")
    app.run_polling()

# Discord bot functions
intents = discord.Intents.default()
intents.message_content = True
discord_bot = commands.Bot(command_prefix="!", intents=intents)
history = load_history()

@discord_bot.event
async def on_ready():
    print(f"Discord bot {discord_bot.user} is connected and running.")

@discord_bot.event
async def on_message(message):
    if message.author == discord_bot.user:
        return  # Ignore messages from the bot itself
    if message.content.startswith("!"):
        user_message = message.content[1:].strip()  # Remove the '!' prefix
        user_id = str(message.author.id)  # Use user ID as string
        response = chat_with_ai(user_message, user_id, history)
        await message.channel.send(response)

@discord_bot.command()
async def reset(ctx):
    user_id = str(ctx.author.id)  # Use user ID as string
    if user_id in history:
        del history[user_id]  # Clear user-specific history
        save_history(history)  # Save the updated history
        await ctx.send("Your conversation history has been reset.")
    else:
        await ctx.send("No conversation history found to reset.")

def run_discord_bot():
    if not discord_token:
        print("Discord token is missing. Skipping Discord bot.")
        return

    print("Discord bot is running. Press Ctrl+C to stop.")
    discord_bot.run(discord_token)

# Local chat function
def run_local_chat():
    print("You are now chatting locally. Type 'exit' to quit.")
    history = load_history()
    user_id = "local_user"  # Use a fixed user ID for local chat
    while True:
        user_message = input("> ").strip()
        if user_message.lower() == "exit":
            print("Exiting local chat.")
            break
        response = chat_with_ai(user_message, user_id, history)
        print(response)

# Main function with mode selection
def main():
    print("Select how you want to run the AI:")
    print(f"{GREEN}1. Local chat{RESET}")
    print(f"{BLUE}2. Bot (Telegram or Discord){RESET}")
    print(f"{RED}3. Go back to main menu{RESET}")

    choice = input(f"{PINK}Enter your choice: {RESET}").strip()

    if choice == '1':
        run_local_chat()
    elif choice == '2':
        print("Select which bot to run:")
        print(f"{BLUE}1. Telegram bot{RESET}")
        print(f"{GREEN}2. Discord bot{RESET}")

        bot_choice = input(f"{PINK}Enter your choice: {RESET}").strip()

        if bot_choice == '1':
            run_telegram_bot()
        elif bot_choice == '2':
            run_discord_bot()
        else:
            print("Invalid choice. Exiting.")
    elif choice == '3':
        # Look for Launcher.py and run it
        if os.path.exists("Launcher.py"):
            print("Going back to main menu...")
            subprocess.run([sys.executable, "Launcher.py"])  # Using sys.executable
        else:
            print("Launcher.py not found. Exiting.")
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
