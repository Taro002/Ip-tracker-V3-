import os
import requests
from time import sleep
from colorama import Fore, Style, init

init(autoreset=True)

WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")
HISTORY_FILE = "history.txt"
API_URL = "http://ip-api.com/json/{}"

LOGO = f"""{Fore.CYAN}
▄▄▄█████▓ ▄▄▄       ██▀███   ▒█████     
▓  ██▒ ▓▒▒████▄    ▓██ ▒ ██▒▒██▒  ██▒   
▒ ▓██░ ▒░▒██  ▀█▄  ▓██ ░▄█ ▒▒██░  ██▒   
░ ▓██▓ ░ ░██▄▄▄▄██ ▒██▀▀█▄  ▒██   ██░   
  ▒██▒ ░  ▓█   ▓██▒░██▓ ▒██▒░ ████▓▒░   
  ▒ ░░    ▒▒   ▓▒█░░ ▒▓ ░▒▓░░ ▒░▒░▒░    
    ░      ▒   ▒▒ ░  ░▒ ░ ▒░  ░ ▒ ▒░    
  ░        ░   ▒     ░░   ░ ░ ░ ░ ▒     
               ░  ░   ░         ░ ░  

        Ip tracker | V.3 by Taro 
{Style.RESET_ALL}"""


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    input(Fore.YELLOW + "\nPress Enter...")


def post_webhook(payload):
    if not WEBHOOK_URL:
        return
    try:
        requests.post(WEBHOOK_URL, json=payload, timeout=5)
    except requests.RequestException:
        pass


def save(data):
    with open(HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(
            f"{data.get('query')} | {data.get('country')} | {data.get('city')} | {data.get('isp')}\n"
        )


def embed(data):
    return {
        "username": "Orbit",
        "embeds": [
            {
                "title": f"IP Lookup — {data.get('query')}",
                "color": 3092790,
                "fields": [
                    {"name": "Country", "value": data.get("country"), "inline": True},
                    {"name": "City", "value": data.get("city"), "inline": True},
                    {"name": "Region", "value": data.get("regionName"), "inline": True},
                    {"name": "ISP", "value": data.get("isp"), "inline": True},
                    {
                        "name": "Maps",
                        "value": f"https://www.google.com/maps?q={data.get('lat')},{data.get('lon')}",
                        "inline": False,
                    },
                ],
            }
        ],
    }


def lookup():
    clear()
    print(LOGO)
    ip = input(Fore.CYAN + "Target IP > ").strip()
    if not ip:
        return

    try:
        res = requests.get(API_URL.format(ip), timeout=10).json()
    except requests.RequestException:
        return

    clear()
    print(Fore.MAGENTA + "RESULT\n")
    for k in ("country", "regionName", "city", "zip", "lat", "lon", "isp", "query"):
        print(f"{k.upper():<12}: {res.get(k, 'N/A')}")

    save(res)
    post_webhook(embed(res))
    pause()


def history():
    clear()
    print(Fore.CYAN + "HISTORY\n")
    if os.path.exists(HISTORY_FILE):
        print(open(HISTORY_FILE, encoding="utf-8").read())
    pause()


def menu():
    while True:
        clear()
        print(LOGO)
        print(
            f"""{Fore.YELLOW}
[1] Lookup IP
[2] History
[0] Exit
"""
        )
        match input("> "):
            case "1":
                lookup()
            case "2":
                history()
            case "0":
                break
        sleep(0.3)


if __name__ == "__main__":
    menu()
