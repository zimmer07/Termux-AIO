import pyfiglet
import os
from colorama import Fore, Style, init

def create_large_termux_text_with_numbers():
    # Initialize colorama
    init(autoreset=True)
    
    # Create the large "Termux-AIO" text
    ascii_art = pyfiglet.figlet_format("Termux-AIO")
    print(ascii_art)
    
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
        {"name": "Install Tor", "url": "https://github.com/SneakBug8/torghost.git"}
    ]
    
    # Print the texts with different colors
    for i, tool in enumerate(tools, start=1):
        color = colors[(i - 1) % len(colors)]
        print(color + f"{i}. {tool['name']}")
    
    # Ask the user to select an option
    try:
        choice = int(input("\nBir seçenek seçin (1-5): "))
        if 1 <= choice <= 5:
            selected_tool = tools[choice - 1]
            print(f"\nSeçtiğiniz seçenek: {selected_tool['name']}")
            # Clone the selected GitHub repository
            os.system(f"git clone {selected_tool['url']}")
            print(f"\n{selected_tool['name']} aracı indirildi.")
        else:
            print("\nGeçersiz seçenek. Lütfen 1 ile 5 arasında bir sayı girin.")
    except ValueError:
        print("\nGeçersiz giriş. Lütfen bir sayı girin.")

if __name__ == "__main__":
    create_large_termux_text_with_numbers()
    