import re, random
from datetime import datetime
from colorama import Fore, init

# Initialize colorama (colorama ensures each print resets after use)
init(autoreset=True)

# destinations = [some data]
destinations = [
    ["Paris", "Midnight", "March"],
    ["Tokyo", "Noon", "August"],
    ["New York", "Evening", "December"],
    ["Sydney", "Morning", "May"]
]

# jokes = [some data]
jokes = [
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do travelers always seem tired? Because of all their jet-lagged journeys!"
]

def normalize_input(user_input):
    return re.sub(r'\s+', ' ', user_input.strip().lower())

def provide_recommendation(user_input):
    normalized_input = normalize_input(user_input)
    print(Fore.CYAN + "TravelBot: Hmm... based on your choices, I suggest:")
    for destination in destinations:
        if normalized_input in destination:
            print(Fore.YELLOW + f"TravelBot: {destination[0]} in {destination[1]} during {destination[2]}")
            return
    print(Fore.RED + "TravelBot: I'll suggest again.")
    recommend()

def recommend():
    suggestion = random.choice(destinations)
    print(Fore.GREEN + f"TravelBot: Awesome! Enjoy {suggestion[0]} in {suggestion[1]} during {suggestion[2]}!")
    print(Fore.YELLOW + "TravelBot: Let's try another.")
    provide_recommendation(input(Fore.YELLOW + "TravelBot: Where would you like to go? "))

def show_help():
    print(Fore.BLUE + "TravelBot: I can suggest travel destinations based on your preferences.")
    print(Fore.BLUE + "TravelBot: You can tell me a destination, time of day, or month.")
    print(Fore.BLUE + "TravelBot: For example, you can say 'Paris in March' or 'Evening in Tokyo'.")
    print(Fore.BLUE + "TravelBot: If you need more help, just type 'help'.")

def tell_a_joke():
    print(Fore.GREEN + "TravelBot: Here's a joke for you:")
    print(Fore.YELLOW + random.choice(jokes))

def main():
    print(Fore.CYAN + "Hello! I'm TravelBot.")
    print(Fore.CYAN + "TravelBot: Nice to meet you. What's your name?")
    name = input(Fore.YELLOW + "Name: ")
    print(Fore.CYAN + f"TravelBot: Hello {name}!")

    while True:
        user_input = input(Fore.YELLOW + f"{name}: ")
        normalized_input = normalize_input(user_input)

        if "recommend" in normalized_input:
            provide_recommendation(user_input)
        elif "help" in normalized_input:
            show_help()
        elif "joke" in normalized_input:
            tell_a_joke()
        elif "exit" in normalized_input:
            print(Fore.RED + "TravelBot: Goodbye!")
            break
        else:
            print(Fore.RED + "TravelBot: Could you rephrase?")

if __name__ == "__main__":
    main()
