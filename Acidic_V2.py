# By 40x50 on GitHub

import requests
import random

from bs4 import BeautifulSoup
from colorama import init, Fore, Style
from os import system
from pygame import mixer

class PeopleFinder:
    def __init__(self, name: str, postal: str):
        self.name = name.replace(" ", "-").lower()
        self.postal = postal

        self.addresses = []
        self.phones = []
        self.aliases = []

        self.headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"} 
        self.r = requests.get(f"https://www.fastpeoplesearch.com/name/{self.name}_{self.postal}", headers=self.headers)
        self.soup = BeautifulSoup(self.r.text, "html.parser")

    def find_all_info(self):
        return self.find_addresses(), self.find_phones(), self.find_aliases()

    def find_addresses(self):
        for a in self.soup.find_all('a', href=True):
            link = str(a).split("href=\"")[1].split("\"")[0]

            if link.startswith("/address/"):
                self.addresses.append(link.split("/address/")[1].replace("-", " "))

        return self.addresses

    def find_phones(self):
        for a in self.soup.find_all('a', href=True):
            link = str(a).split("href=\"")[1].split("\"")[0]

            try:
                number = int(link[1:].replace("-", ""))
                self.phones.append(str(number))
            except:
                pass
        
        return self.phones
    
    def find_aliases(self):
        for a in self.soup.find_all("span", class_="nowrap")[1:]:
            try:
                alias = str(a).split("<span class=\"nowrap\">")[1].split("</span>")[0]
                self.aliases.append(alias)
            except:
                pass
        
        return self.aliases

init(convert=True)

def logo():
    try:
        system("cls")
    except:
        system("clear")

    print(
        Style.BRIGHT + f"""
        {Fore.BLUE + "          "}{Fore.CYAN + "         "}{Fore.GREEN + "    "}{Fore.MAGENTA + "        "}{Fore.RED + "     "}{Fore.YELLOW + "        "}
        {Fore.BLUE + " ▄▄▄      "}{Fore.CYAN + " ▄████▄  "}{Fore.GREEN + " ██▓"}{Fore.MAGENTA + "▓█████▄ "}{Fore.RED + " ██▓ "}{Fore.YELLOW + "▄████▄  "}
        {Fore.BLUE + "▒████▄    "}{Fore.CYAN + "▒██▀ ▀█  "}{Fore.GREEN + "▓██▒"}{Fore.MAGENTA + "▒██▀ ██▌"}{Fore.RED + "▓██▒▒"}{Fore.YELLOW + "██▀ ▀█  "}
        {Fore.BLUE + "▒██  ▀█▄  "}{Fore.CYAN + "▒▓█    ▄ "}{Fore.GREEN + "▒██▒"}{Fore.MAGENTA + "░██   █▌"}{Fore.RED + "▒██▒▒"}{Fore.YELLOW + "▓█    ▄ "}
        {Fore.BLUE + "░██▄▄▄▄██ "}{Fore.CYAN + "▒▓▓▄ ▄██▒"}{Fore.GREEN + "░██░"}{Fore.MAGENTA + "░▓█▄   ▌"}{Fore.RED + "░██░▒"}{Fore.YELLOW + "▓▓▄ ▄██▒"}
        {Fore.BLUE + " ▓█   ▓██▒"}{Fore.CYAN + "▒ ▓███▀ ░"}{Fore.GREEN + "░██░"}{Fore.MAGENTA + "░▒████▓ "}{Fore.RED + "░██░▒"}{Fore.YELLOW + " ▓███▀ ░"}
        {Fore.BLUE + " ▒▒   ▓▒█░"}{Fore.CYAN + "░ ░▒ ▒  ░"}{Fore.GREEN + "░▓  "}{Fore.MAGENTA + " ▒▒▓  ▒ "}{Fore.RED + "░▓  ░"}{Fore.YELLOW + " ░▒ ▒  ░"}
        {Fore.BLUE + "  ▒   ▒▒ ░"}{Fore.CYAN + "  ░  ▒   "}{Fore.GREEN + " ▒ ░"}{Fore.MAGENTA + " ░ ▒  ▒ "}{Fore.RED + " ▒ ░ "}{Fore.YELLOW + " ░  ▒   "}
        {Fore.BLUE + "  ░   ▒   "}{Fore.CYAN + "░        "}{Fore.GREEN + " ▒ ░"}{Fore.MAGENTA + " ░ ░  ░ "}{Fore.RED + " ▒ ░░"}{Fore.YELLOW + "        "}
        {Fore.BLUE + "      ░  ░"}{Fore.CYAN + "░ ░      "}{Fore.GREEN + " ░  "}{Fore.MAGENTA + "   ░    "}{Fore.RED + " ░  ░"}{Fore.YELLOW + " ░      "}
        {Fore.BLUE + "          "}{Fore.CYAN + "░        "}{Fore.GREEN + "    "}{Fore.MAGENTA + " ░      "}{Fore.RED + "    ░"}{Fore.YELLOW + "        "}
        {Fore.BLUE + "          "}{Fore.CYAN + "         "}{Fore.GREEN + "    "}{Fore.MAGENTA + "        "}{Fore.RED + "     "}{Fore.YELLOW + "        "}
        \n"""
    )

save_output = False
music = True
music_tog = True

mixer.init()
mixer.music.load("music.wav")
mixer.music.set_volume(0.1)

system("title AcidicV2 People Researcher")

while True:
    ran = random.randint(0, 100)

    if music:
        if music_tog:
            mixer.music.play()
            music_tog = False
    else:
        mixer.music.stop()

    logo()

    print(
    Fore.CYAN + f"""
    \t\tOptions
    ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
    █ {Fore.GREEN + "[1] Reseacher"}                {Fore.CYAN + "█"}
    {Fore.CYAN + "█"} {Fore.BLUE + "[2] Settings"}                 {Fore.CYAN + "█"}
    {Fore.CYAN + "████████████████████████████████"}
    \n"""
    )

    print(">: ", end="")
    menu = input("")

    if menu == "1":
        logo()

        print(Fore.CYAN + "\nEnter person's name >: ", end="")
        name = input("").replace(" ", "-").lower()

        print("Enter person's postal code >: ", end="")
        postal = input("")

        finder = PeopleFinder(name, postal)
        addresses, phones, aliases = finder.find_all_info()

        for i, v in enumerate(addresses):
            if save_output:
                with open(f"output{ran}.txt", "a") as f:
                    f.write(v + "\n")

            if i == 0:
                print(Fore.GREEN + "\nMain Address          : " + v)
            else:
                print(Fore.RED + "Other Possible Address: " + v)

        for i, v in enumerate(phones):
            if save_output:
                with open(f"output{ran}.txt", "a") as f:
                    f.write(v + "\n")

            if i == 0:
                print(Fore.GREEN + "\nMain Phone           : " + v)
            else:
                print(Fore.RED + "Other Possible Phones: " + v)

        print(Fore.BLUE + "\n")

        for x in aliases:
            if save_output:
                with open(f"output{ran}.txt", "a") as f:
                    f.write(v + "\n")

            print("Possible Alias: " + x)
        
        input("\n\nPress ENTER to clear...")
    if menu == "2":
        logo()
        print(
    Fore.CYAN + f"""
    \t\tOptions
    ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
    █ {Fore.GREEN + "[1] Save Output: " + str(save_output)}       {Fore.CYAN + "█"}
    {Fore.CYAN + "█"} {Fore.BLUE + "[2] Music: " + str(music)}              {Fore.CYAN + "█"}
    {Fore.CYAN + "████████████████████████████████"}
    \n"""
        )

        print(">: ", end="")
        option = input("")

        if option == "1":
            print("Save Output: \"y\" or \"n\" >: ", end="")
            save_output = input("")
            
            if save_output == "y":
                save_output = True
            else:
                save_output = False
            
        if option == "2":
            print("Music: \"y\" or \"n\" >: ", end="")
            music = input("")

            if music == "y":
                music = True
                music_tog = True
            else:
                music = False