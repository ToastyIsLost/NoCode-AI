import os
import subprocess
import time
import itertools

# ANSI color codes
COLORS = [
    "\033[91m",  # Red
    "\033[93m",  # Yellow
    "\033[92m",  # Green
    "\033[96m",  # Cyan
    "\033[94m",  # Blue
    "\033[95m",  # Magenta
]
RESET = "\033[0m"
BOLD = "\033[1m"

def rainbow_text(text):
    """Yields the text with cycling colors."""
    color_cycle = itertools.cycle(COLORS)
    for char in text:
        yield f"{next(color_cycle)}{char}{RESET}"

def print_rainbow_banner():
    """Displays the banner with a rainbow effect."""
    banner = """
     _   _     __                        _               
  /_\ (_)   / /  __ _ _   _ _ __   ___| |__   ___ _ __ 
 //_\\| |  / /  / _` | | | | '_ \ / __| '_ \ / _ \ '__|
/  _  \ | / /__| (_| | |_| | | | | (__| | | |  __/ |   
\_/ \_/_| \____/\__,_|\__,_|_| |_|\___|_| |_|\___|_|   
    """
    for line in banner.splitlines():
        print("".join(rainbow_text(line)))
        time.sleep(0.1)  # Add delay for smoother animation

def main_menu():
    while True:
        print(f"\n{BOLD}Main Menu{RESET}")
        print(f"{COLORS[2]}1. Run the main bot script{RESET}")
        print(f"{COLORS[4]}2. Configure API keys and identity{RESET}")
        print(f"{COLORS[0]}3. Exit{RESET}")

        choice = input(f"{COLORS[5]}Enter your choice: {RESET}").strip()

        if choice == '1':
            run_main_script()
        elif choice == '2':
            run_configuration()
        elif choice == '3':
            print(f"{COLORS[1]}Exiting the launcher. Goodbye!{RESET}")
            break
        else:
            print(f"{COLORS[0]}Invalid choice. Please try again.{RESET}")

def run_main_script():
    print(f"{COLORS[3]}Launching the main bot script...{RESET}\n")
    subprocess.run(["python3", "run.py"])

def run_configuration():
    print(f"{COLORS[4]}Launching the configuration tool...{RESET}\n")
    subprocess.run(["python3", "configure.py"])

if __name__ == "__main__":
    print_rainbow_banner()
    main_menu()
