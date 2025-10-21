import colorama
from colorama import Fore, Style
from textblob import TextBlob

# Initialize colorama for colored output
colorama.init()

# Emojis for the start of the program
print(f"{Fore.RED}💥🤖 Hello! Welcome to Sentiment Spy! 💥{Style.RESET_ALL}")

name = input(f"{Fore.CYAN}What is your name?  {Style.RESET_ALL} ").strip()
if not name:
    name = "Anonymous Agent" 

# Store conversation as a list of tuples: (text, polarity, sentiment_type)
conversation_history = []

print(f"\n{Fore.CYAN}Hello, {name}!")
print(f"{Fore.YELLOW}Type a Sentence and I will analyze the sentiment of your sentence. 💬")
print(f"{Fore.YELLOW}Type '{Fore.CYAN}reset{Fore.YELLOW}', '{Fore.CYAN}history{Fore.YELLOW}', "
      f"or '{Fore.CYAN}exit{Fore.YELLOW}' to quit.{Style.RESET_ALL}\n")

while True:
    user_input = input(f"{Fore.GREEN}>> {Style.RESET_ALL}").strip()

    if not user_input:
        print(f"{Fore.RED}Please enter some text.{Style.RESET_ALL}")
        continue

    # Check for commands
    if user_input.lower() == "exit":
        print(f"\n{Fore.CYAN}🕵️ Exiting Sentiment Spy. Farewell, Agent {name}! 🫡{Style.RESET_ALL}")
        break

    elif user_input.lower() == "reset":
        conversation_history.clear()
        print(f"{Fore.YELLOW}♻️ All conversation history cleared!{Style.RESET_ALL}")
        continue

    elif user_input.lower() == "history":
        if not conversation_history:
            print(f"{Fore.MAGENTA}No conversation history yet.{Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN}📜 Conversation History:{Style.RESET_ALL}")
            for index, (emoji, text, polarity, sentiment_type) in enumerate(conversation_history, start=1):
                # Choose color & emoji based on sentiment
                if sentiment_type == "Positive":
                    color = Fore.GREEN
                elif sentiment_type == "Negative":
                    color = Fore.RED
                else:
                    color = Fore.YELLOW
                print(f"{index}. {emoji} {color}{text} (Polarity : {polarity: 0.2f}, {sentiment_type}){Style.RESET_ALL} ")
        continue

    # Analyze sentiment
    polarity = TextBlob(user_input).sentiment.polarity
    if polarity > 0.25:
        sentiment_type = "Positive"
        color = Fore.GREEN
        emoji = ":)"
    elif polarity < -0.25:
        sentiment_type = "Negative"
        color = Fore.RED
        emoji = ":("
    else:
        sentiment_type = "Neutral"
        color = Fore.YELLOW
        emoji = ":|"

    # Store in history
    conversation_history.append((emoji, user_input, polarity, sentiment_type))

    # Print result with color, emojis, and polarity
    print(f"{color}{emoji} {sentiment_type} sentiment detected! "
          f"(Polarity: {polarity:.2f}){Style.RESET_ALL}")
