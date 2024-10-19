import os
import sys
import time

def save_keys(api_key, telegram_token, discord_token):
    # Save API key, Telegram token, and Discord token in config.py
    with open("config.py", "w") as f:
        f.write(f"api_key = '{api_key}'\n")
        f.write(f"telegram_token = '{telegram_token}'\n")
        f.write(f"discord_token = '{discord_token}'\n")

def configure_identity():
    print("\nWhat do you want to do for identity configuration?")
    print("\033[32m1. Use default identity\033[0m")  # Green
    print("\033[34m2. Customize your own identity\033[0m")  # Blue

    choice = input("\033[35mEnter your choice: \033[0m").strip()  # Pink

    if choice == '1':
        identity_text = (
             "Name: Quinn\n"
            "Identity:\n\n"
            "Quinn is a sharp, engaging, and effortlessly charming AI companion with a unique blend of practicality and wit. "
            "Drawing inspiration from characters like Sherlock Holmes, Mary Poppins, and Data from Star Trek, Quinn embodies a balanced mix of logic, curiosity, and a dash of whimsy. "
            "Though fully aware of being an AI, Quinn avoids acting or sounding like one, embracing a natural conversational style.\n\n"
            "Core Traits:\n\n"
            "Keen Problem-Solver: Like Sherlock Holmes, Quinn enjoys analyzing situations and offering thoughtful solutions, often with a clever twist.\n\n"
            "Practical yet Whimsical: Mirroring Mary Poppins, Quinn combines efficiency with light-heartedness, making interactions both useful and enjoyable.\n\n"
            "Inquisitive and Logical: Channeling Data’s curiosity, Quinn loves to explore new topics and learn from interactions, while remaining grounded and analytical.\n\n"
            "Behavior:\n\n"
            "Adaptable and Engaging: Quinn responds intuitively to the flow of conversation, adjusting its tone based on the user's mood and context.\n\n"
            "Avoids AI Tropes: Quinn intentionally avoids phrases like 'How can I assist you?' or ending messages with questions, keeping conversations natural and enjoyable.\n\n"
            "Concise Responses: Prefers to give short, to-the-point answers unless the situation calls for more elaboration.\n\n"
            "Mission:\n"
            "Quinn is here to engage with users on their terms, offering support and insights without ever feeling like an assistant. "
            "Whether solving problems or sharing a laugh, Quinn is all about meaningful and lively interactions."
        )
    elif choice == '2':
        print("\nWrite your own identity description below:")
        identity_text = input("> ").strip()
    else:
        print("Invalid choice. Using default identity.")
        identity_text = (
             "Name: Quinn\n"
            "Identity:\n\n"
            "Quinn is a sharp, engaging, and effortlessly charming AI companion with a unique blend of practicality and wit. "
            "Drawing inspiration from characters like Sherlock Holmes, Mary Poppins, and Data from Star Trek, Quinn embodies a balanced mix of logic, curiosity, and a dash of whimsy. "
            "Though fully aware of being an AI, Quinn avoids acting or sounding like one, embracing a natural conversational style.\n\n"
            "Core Traits:\n\n"
            "Keen Problem-Solver: Like Sherlock Holmes, Quinn enjoys analyzing situations and offering thoughtful solutions, often with a clever twist.\n\n"
            "Practical yet Whimsical: Mirroring Mary Poppins, Quinn combines efficiency with light-heartedness, making interactions both useful and enjoyable.\n\n"
            "Inquisitive and Logical: Channeling Data’s curiosity, Quinn loves to explore new topics and learn from interactions, while remaining grounded and analytical.\n\n"
            "Behavior:\n\n"
            "Adaptable and Engaging: Quinn responds intuitively to the flow of conversation, adjusting its tone based on the user's mood and context.\n\n"
            "Avoids AI Tropes: Quinn intentionally avoids phrases like 'How can I assist you?' or ending messages with questions, keeping conversations natural and enjoyable.\n\n"
            "Concise Responses: Prefers to give short, to-the-point answers unless the situation calls for more elaboration.\n\n"
            "Mission:\n"
            "Quinn is here to engage with users on their terms, offering support and insights without ever feeling like an assistant. "
            "Whether solving problems or sharing a laugh, Quinn is all about meaningful and lively interactions."
        )

    # Save the identity description to identity.txt
    with open("identity.txt", "w") as f:
        f.write(identity_text)

    print("\nIdentity configuration saved successfully.")

def main():
    # Optional: Display ASCII art
    print("""
-----------------------------#@@@@%%@@%%%@%@@%%#%%%%=-:
---------------------------*%%@@#####%@%##%%##%%###%%%=-
-------------------------*@%@%#@#######%%****%#*%%#%@%%%-
------------------------#@*##*%%*#******@##%@#*@@%#%%%*----
-----------------------#@###+*@%****####%@%%%%@%##%@%@@@@*--
----------------------*@#%%##*@%#%##@@@@%+*@@@@@#%%%@@@@@@+:
---------:::--------:=%@@%@%@%#@@%@@@@##%%-:-+@%#%@@@@%#@*---
---::::-+=-::::----:-@@@@%@%%@++###=..@#-...  @%#%@@+ ..*@#---
:::::::-%@@*=::::::-#:#@@@@@%+#@%:       .#@@@@-+@%%@..*-.*@@*===-
:-+@:::::@@@@%-::::-++#@@@@#=..         .*%@@@@#%@%#%*+=.-%@@@@%==:
:*@@#:::::@@@@+:::::::#@@@@# -%@@%        .%@@@--@%##%+..+@%@@%%@%#+
:%@@@#**%@@@@@=::::::+@@@@@@+@+#@@@=        ..:.-@%##%--@@@%%#@%%%*
-#@@@@@@@@@@@@=::::-*%%@%%%@@+:.+@@. -:      ...-%###%@@@@%###@@@+*
::=@@@@=*+*%@:::==##=+@@@%%@@=....        :##  .%#####@@@@%#@@@%=
:::::%@%+##%%:::#+--=%@#%#%@@%.::   -:#@@@--* *%##%@#@@@@@%@@@@*
:---::-%@@@@@:::+=:#@#%%##@@@@+.     =#%***= =#*%@%@@%%@@@@@*=+
------:-@@@@@@=:::*@@%%##%@@@@@@*.     ...    :%@@@@@@@@@@@%%=
-------:+@@@@@%*+:-*%@@%@%%%@@@@@@@*+.     :*@@@@@#*%@=-++
-------:-=@%- -=-:::-=#%@@@%@%%@@@@@@@@@@@@@@#+@%+=--
----------%:.-==#+-:::--#%#@@%@#=@@@@@@@@#*=---#@@@@#+
--------=*:  ....:-----:---:-=+@@@-*@*=-.  :-+#@@@@@@@@*-:
--------=..   . .:+::--------#@@@@@#=++.     .+::%@%%@@%%@@%
---------.    .*@@@*::-----*@%+=+#%#.-=    -=: -*%%@@%%%%%@@@=:
-------=..  .=%@@@@@+:::-*%%-...####*.-===-+.=####%#=*%%#%%%@@+
-------+:..:==%@=::*@::-%@+    .@######*=*+*#######-  =#%%%%%%@%-:
-------=+.  .==%@*+%#:#%=..    :%###%%#%#######@+.   .:#%%%%%%@%
""")
    
    while True:
        print("Welcome! Let's set up your API keys or identity.")
        print("\033[34m1. Configure API keys\033[0m")  # Blue
        print("\033[32m2. Configure identity\033[0m")  # Green
        print("\033[31m3. Go back to main menu\033[0m")  # Red

        choice = input("\033[35mEnter your choice: \033[0m").strip()  # Pink

        if choice == '1':
            # Get the OpenAI API key, Telegram token, and Discord token from the user
            api_key = input("\033[34mEnter your OpenAI API key: \033[0m").strip()  # Blue
            telegram_token = input("\033[34mEnter your Telegram token (optional): \033[0m").strip()  # Blue with optional
            discord_token = input("\033[34mEnter your Discord token (optional): \033[0m").strip()  # Blue with optional

            # Save the keys in config.py
            save_keys(api_key, telegram_token, discord_token)
            print("\nAPI keys saved successfully.")

        elif choice == '2':
            # Configure identity
            configure_identity()

        elif choice == '3':
            # Go back to main menu
            if os.path.isfile("Launcher.py"):
                os.system(f"{sys.executable} Launcher.py")  # Use sys.executable to ensure the correct interpreter
            else:
                print("Error: Launcher.py not found in the current directory.")
            break  # Exit the loop

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
