import pyfiglet
import os
from colorama import Fore, Style, init

def create_large_termux_text_with_numbers():
    # Initialize colorama
    init(autoreset=True)
    
    # Create the large "Termux-AIO" text
    ascii_art = pyfiglet.figlet_format("Termux-AIO")
    print(Fore.RED + ascii_art)
    
    # Made By; Zimmer07
    print(Fore.BLUE + "Made By; Zimmer07\n")
    
    # Define colors for numbers
    colors = [
        Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE,
        Fore.MAGENTA
    ]
    
    # Define the texts and corresponding GitHub URLs
    tools = [
        {"name": "Zphisher", "url": "https://github.com/htr-tech/zphisher.git"},
        {"name": "IP-Tracer", "url": "https://github.com/Rajkumrdusad/IP-Tracer.git"},
        {"name": "Fast Sms Bomber", "url": "https://github.com/LimerBoy/Impulse.git"},
        {"name": "Brute Force", "url": "https://github.com/vanhauser-thc/thc-hydra.git"},
        {"name": "Install Tor", "url": "https://github.com/SneakBug8/torghost.git"},
        {"name": "Metasploit Framework", "url": "https://github.com/rapid7/metasploit-framework.git"},
        {"name": "Nmap", "url": "https://github.com/nmap/nmap.git"},
        {"name": "SQLMap", "url": "https://github.com/sqlmapproject/sqlmap.git"},
        {"name": "OSINT", "url": "https://github.com/soxoj/osint.git"},
        {"name": "Keylogger", "url": "https://github.com/Drecc/chrome-keylogger.git"}
    ]
    
    # Print the texts with different colors
    for i, tool in enumerate(tools, start=1):
        color = colors[(i - 1) % len(colors)]
        print(color + f"{i}. {tool['name']}")
    
    # Ask the user to select an option
    try:
        choice = int(input("\nChoose an option (1-10): "))
        if 1 <= choice <= 10:
            selected_tool = tools[choice - 1]
            print(f"\nYou selected: {selected_tool['name']}")
            # Clone the selected GitHub repository
            os.system(f"git clone {selected_tool['url']}")
            print(f"\n{selected_tool['name']} tool has been downloaded.")
        else:
            print("\nInvalid option. Please enter a number between 1 and 10.")
    except ValueError:
        print("\nInvalid input. Please enter a number.")

if __name__ == "__main__":
    create_large_termux_text_with_numbers()
