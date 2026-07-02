#!/usr/bin/env python3

import subprocess

# colors for text :)
blue = "\033[94m"
red = "\033[91m"
green = "\033[92m"
reset = "\033[0m"

# handles the first prompt
def ft_welcome_print():
    print(f"\n=== Welcome to {blue}dock_mod{reset}! ===\n")
    return input("Speed up dock (1) or reset to default (0)? (enter q to quit)\n\n")

# Either runs command to speed up dock or puts its value to default
def ft_dock_mod():
    usr_input = ft_welcome_print()
    if usr_input == "1":
        speed = input("Animation speed (0-1) [default 0.15]: ") or "0.15"
        subprocess.run(f"""
            defaults write com.apple.dock autohide-delay -float 0;
            defaults write com.apple.dock autohide-time-modifier -float {speed};
            defaults write com.apple.dock autohide-fullscreen-delayed -bool false;
            killall Dock
        """, shell=True)
        print(f"{green}Speedy dock: activated!{reset}")
    elif usr_input == "0":
        subprocess.run("""
            defaults delete com.apple.dock autohide-delay;
            defaults delete com.apple.dock autohide-time-modifier;
            defaults delete com.apple.dock autohide-fullscreen-delayed;
            killall Dock
        """, shell=True)
        print(f"{green}Speedy dock: deactivated...{reset}")
    elif usr_input == "q":
        return
    else:
        print (f"{red}Invalid input, try again{reset}")
        ft_dock_mod()


if __name__ == "__main__":
    ft_dock_mod()
