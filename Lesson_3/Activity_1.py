import re, random
from colorama import Fore, init

# Initialize colorama (autoreset ensures each print resets after use)
init(autoreset=True)

# Destination & joke data
destinations = {
    "beaches": ["Bali", "Maldives", "Phuket", "Bahamas", "Canon Beach", "Clifton Beach"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas", "Karakoram", "Atlas", "Everest"],
    "cities": ["Tokyo", "Paris", "New York", "Istanbul", "Venice", "Rome", "Edinburgh"]
}

jokes = [
    "Why don't programmers like nature? Too many bugs!",
    "How did the first program die? Because It was executed.",
    "Whats the object-oriented way to become wealthy? Inheritance!"
]

safety_tips = [
    "Always check the limit for your luggage to avoid any trouble."
    "Call your family frequently and let them know your location.",
    "Don't interact too much with strangers and never take aything from them.",
    "Always use maps and first check for reviews before checking into any hotel.",
    "Make sure your phone's location is always on so that it could be traced."
]

packing_tips = [
    "Pack versatile clothes."
    "Bring chargers/adapters."
    "Check the weather forecast."
    "Pack something to eat and drink."
    "Always carry sanitary bag with you."
]

# Helper function to normalize user input (remove extra spaces, make lowercase)
def normalize_input(text):
    return re.sub(r"\s+", " ", text.strip().lower())

# Provide travel recommendations (recursive if user rejects suggestions)
def recommend_destination():
    print(Fore.MAGENTA + "TravelBot: Beaches, mountains, or cities?")
    selection = input(Fore.YELLOW + "You: ")
    selection = normalize_input(selection)

    if selection in destinations:
        suggestion = random.choice(destinations[preference])
        print(Fore.GREEN + f"TravelBot: How about {suggestion}?")
        print(Fore.CYAN + "TravelBot: Do you like it? (yes/no)")
        answer = input(Fore.YELLOW + "You: ").lower()

        if answer == "yes":
            print(Fore.GREEN + f"TravelBot: Awesome! Enjoy {suggestion}!")
        elif answer == "no":
            print(Fore.RED + "TravelBot: Let's try again.")
            recommend_destination()
        else:
            print(Fore.RED + "TravelBot: I'll suggest again.")
            recommend_destination()
    else:
        print(Fore.RED + "TravelBot: Sorry, I don't have knwledge regarding this location.")
        show_menu()

# Offer packing tips based on user's destination and duration
def packing_Tips():
    print(Fore.CYAN + "TravelBot: Where are you planning to travel?")
    location = normalize_input(input(Fore.YELLOW + "You: "))
    print(Fore.CYAN + "TravelBot: For how many days?")
    days = input(Fore.YELLOW + "You: ")
    print(Fore.GREEN + f"TravelBot: Packing tips for {days} days in {location}:")
    for tip in safety_tips:
        print(f"{Fore.GREEN} - {tip}")
    

def safety_Tips():
    print(f"{Fore.YELLOW} Here are some safety tips for you:")
    for tip in safety_tips:
        print(f"{Fore.GREEN} {tip}")

    print(f"{Fore.YELLOW} Have a safe journey!")

# Tell a random joke
def tell_joke():
    print(Fore.YELLOW + f"TravelBot: {random.choice(jokes)}")

# Display help menu
def show_menu():
    print(Fore.MAGENTA + "\nI can:")
    print(Fore.GREEN + "- Suggest travel spots (say 'recommend')")
    print(Fore.GREEN + "- Offer packing tips (say 'packing')")
    print(Fore.GREEN + "- Describe Safety measures (say 'safety')")
    print(Fore.GREEN + "- Tell a joke (say 'joke')")
    print(Fore.GREEN + "- Type 'exit' or 'bye' to end.\n")

# Main chat loop
def chat():
    print(Fore.CYAN + "Hello! I'm TravelBot. I'll help you with your travel.")
    name = input(Fore.YELLOW + "What is your name? ")
    print(Fore.GREEN + f"Nice to meet you, {name}!")

    show_menu()

    while True:
        user_input = input(Fore.YELLOW + f"{name}: ")
        user_input = normalize_input(user_input)

        if "recommend" in user_input or "suggest" in user_input:
            recommend_destination()
        elif "pack" in user_input or "packing" in user_input:
            packing_Tips()
        elif "joke" in user_input or "funny" in user_input:
            tell_joke()
        elif "safety" in user_input or "precautions" in user_input:
            safety_Tips()
        elif "help" in user_input:
            show_menu()
        elif "exit" in user_input or "bye" in user_input:
            print(Fore.CYAN + "TravelBot: Safe travels! Goodbye!")
            break
        else:
            print(Fore.RED + "TravelBot: Could you rephrase?")

# Run the chatbot
if __name__ == "__main__":
    chat()
