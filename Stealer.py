from pyrogram import Client
from colorama import Fore, Style
import sys
from time import sleep
from colorama import init, Fore, Style
from os import system, name
from random import choice
from threading import Thread
from requests import get
init()

client = Client("spad_sec", api_id=1867281, api_hash="bac3dd5c231f1d69d8679174de34fe45")
client.start()

is_steal = False


class SpadSec:
    colors = [Fore.RED, Fore.BLUE, Fore.WHITE, Fore.GREEN, Fore.CYAN, Fore.YELLOW]
    def cleaner(self):
        if name == "nt":
            system("cls")
        else:
            system("clear")
    
    def logo_printer(self):
        self.cleaner()
        logo = """
███████╗██████╗  █████╗ ██████╗ ███████╗███████╗ ██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
███████╗██████╔╝███████║██║  ██║███████╗█████╗  ██║     
╚════██║██╔═══╝ ██╔══██║██║  ██║╚════██║██╔══╝  ██║     
███████║██║     ██║  ██║██████╔╝███████║███████╗╚██████╗
╚══════╝╚═╝     ╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝ ╚═════╝
            Telegram Username Stealer v2.0
                  github.com/L0C4L
                    t.me/SpadSEC

        """
        _logo_enumer = 0
        for char in logo:
            if _logo_enumer <= 343:
                sys.stdout.write(f"{choice(self.colors)}{char}{Style.RESET_ALL}")
                sys.stdout.flush()
                _logo_enumer +=1
                sleep(0.002)
            else:
                sys.stdout.write(f"{self.colors[3]}{char}{Style.RESET_ALL}")
                sys.stdout.flush()
                sleep(0.002)


class Stealer:
    def CreateChannel(self, username):
        channel = client.create_channel("SpadStealer", "SpadUsernameStealer")
        client.update_chat_username(channel.id, username)
        client.stop()

def checker(user):
    while True:
        _conn = get(f"https://t.me/{user}", timeout=5)
        if "</a> right away." in _conn.text:
            print("Stealed")
            client.start()
            sleep(2)
            steal = Stealer()
            steal.CreateChannel(user)
            break

if __name__ == "__main__":
    try:
        client.stop()
        logo = SpadSec()
        logo.logo_printer()
        try:
            username = sys.argv[1]
            try:
                with open(username, mode="r", encoding="UTF-8") as usernames:
                    usernames = usernames.read().splitlines()
            except FileNotFoundError:
                print(f"{Fore.YELLOW}File not Found{Style.RESET_ALL}")
                sys.exit(True)
        except IndexError:
            print(f"{Fore.YELLOW}Usage: {Fore.GREEN}python {Fore.CYAN}{sys.argv[0]} {Fore.GREEN}usernames.txt{Style.RESET_ALL}")
            sys.exit(True)
        for data in usernames:
            Thread(target=checker, args=(data,)).start()
            sleep(1)
    except KeyboardInterrupt:
        print("\nGoodBye <3")
