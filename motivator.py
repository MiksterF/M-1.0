import random
import datetime
from colorama import Fore, Style, init

# Inicjalizacja kolorów w konsoli (działa też na Windows)
init(autoreset=True)

quotes = [
    "Nie czekaj na idealny moment. Weź moment i spraw, by był idealny.",
    "Każdy dzień to nowa szansa, by zacząć od nowa.",
    "Nie musisz być wielki, żeby zacząć. Ale musisz zacząć, żeby być wielki.",
    "Sukces to suma małych wysiłków powtarzanych każdego dnia.",
    "Uwierz, że możesz – a już jesteś w połowie drogi.",
    "Zrób dziś coś, z czego jutro będziesz dumny.",
    "Twoje myśli tworzą Twoją rzeczywistość. Wybieraj je mądrze."
]

def show_quote():
    today = datetime.date.today()
    quote = random.choice(quotes)

    print(Fore.CYAN + Style.BRIGHT + "\n🌞 MOTYWATOR DNIA 🌞")
    print(Fore.YELLOW + f"\n📅 {today.strftime('%A, %d %B %Y')}\n")
    print(Fore.GREEN + f"💬 {quote}\n")
    print(Fore.MAGENTA + "— Pamiętaj: małe kroki też prowadzą na szczyt —\n")

def add_quote():
    new_quote = input("Wpisz swój cytat: ").strip()
    if new_quote:
        quotes.append(new_quote)
        print(Fore.GREEN + "✅ Dodano nowy cytat!")
    else:
        print(Fore.RED + "⚠️ Nie wpisano żadnego cytatu.")

def main():
    while True:
        print(Fore.CYAN + "\n=== MOTYWATOR DNIA ===")
        print("1️⃣  Pokaż losowy cytat")
        print("2️⃣  Dodaj własny cytat")
        print("3️⃣  Wyjdź")

        choice = input("\nWybierz opcję: ")

        if choice == "1":
            show_quote()
        elif choice == "2":
            add_quote()
        elif choice == "3":
            print(Fore.BLUE + "👋 Do zobaczenia! Niech Twój dzień będzie dobry!")
            break
        else:
            print(Fore.RED + "Nieprawidłowy wybór. Spróbuj ponownie.")

if __name__ == "__main__":
    main()
