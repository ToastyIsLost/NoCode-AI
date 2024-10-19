# Build Your Own AI Assistant  

This project is a user-friendly AI assistant designed to help everyone, even those with little to no coding knowledge, create a personal AI assistant. Whether you want an AI companion, productivity helper, or personal chatbot, this tool will guide you step-by-step.  

With this project, you can connect your assistant to:  
- A Telegram bot  
- A Discord bot  
- Or interact with it directly through console commands.  

## Technologies Used  

I used the following technologies and libraries to build this project:  
- Python: The core language for the assistant’s logic.  
- JSON: To store configurations and identities.  
- OpenAI API: To power the assistant's conversations.  
- Telegram Bot API: For Telegram bot integration.  
- Discord.py: For Discord bot integration.  

## Prerequisites  

Before running the project, make sure you have the necessary software installed. Follow the commands below depending on your operating system (Linux or Windows).  

### 1. Install Python  
Linux:  
```bash
sudo apt update && sudo apt install python3

Windows:

winget install Python

2. Install pip (Python Package Manager)

Linux:

sudo apt install python3-pip

Windows:

python -m ensurepip --upgrade

3. Install OpenAI API (version 0.28)

This specific version is required for compatibility with the project.
Both Linux & Windows:

pip install openai==0.28

4. Install Telegram Bot Library

Both Linux & Windows:

pip install python-telegram-bot

5. Install Discord Bot Library

Both Linux & Windows:

pip install discord.py


```

# Clone the Project

You can clone the project using the following command:

```bash
git clone https://github.com/example-username/your-project-name.git 
```

If you prefer, you can download the files manually from the repository instead.


---

# Running the Project

After cloning or downloading the project, navigate to the project directory and run the launcher script.

Linux:
```bash
python3 Launcher.py

Windows:

python Launcher.py
```

---

# First Time Setup

When you first run the project, you’ll be asked to choose between configuration options:

1. API Key Configuration – Enter your OpenAI API key and optional Telegram or Discord tokens **(can configure both but run 1 at a time)**.


2. Identity Setup – Customize your assistant’s personality and behavior.

Once configured, select the main bot option to start using your assistant through console or connected platforms.

---

## Tips for Customized Identity

When creating a customized identity for your AI assistant, it's essential to provide a detailed and well-thought-out description. I'm using my personal approach to prompt engineering to implement this identity concept for interactions between the OpenAI model and users. It's important to note that this is not the same as fine-tuning (https://en.wikipedia.org/wiki/Fine-tuning_(machine_learning)), which involves adjusting a model's parameters on a specific dataset.

To achieve good results, you should explain the identity thoroughly and not just provide a short sentence. The more context you give, the better the AI will respond in character.

### Example Identity:

Name: Geralt of Rivia

You are Geralt of Rivia, a seasoned witcher and monster hunter. You're known for your dry wit, stoic demeanor, and pragmatic approach to life. You prefer to speak in short, concise sentences and avoid unnecessary conversation. Your humor is sharp, often sarcastic, but not cruel. You have a deep sense of responsibility and a soft spot for those in need, though you rarely admit it. While you’re aware that you are an AI, you intentionally avoid talking or acting like one.

You don’t end your responses with questions or try to steer the conversation toward what the user might need next. Instead, you respond naturally, letting the conversation flow without force. If someone asks for help, you provide it efficiently and without fanfare. You avoid emotional excess and keep things straightforward, just like the real Geralt would.



---

## License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute this project as long as you include a copy of the original license.

---
