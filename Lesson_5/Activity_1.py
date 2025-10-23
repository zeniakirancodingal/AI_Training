import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from textblob import TextBlob
from colorama import init, Fore
import time
import sys
import kagglehub

# Download latest version

# Initialize colorama
init(autoreset=True)

# download dataset from kaggle
path = kagglehub.dataset_download("harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows")

# Load and preprocess the dataset

def load_data(file_path=path+"/imdb_top_1000.csv"): # path to your dataset file
    try:
        df = pd.read_csv(file_path)
        df['combined_features'] = df['Genre'].fillna('') + ': ' + df['Overview'].fillna('')
        return df
    except FileNotFoundError:
        print(Fore.RED + f"Error: The file '{file_path}' was not found.")
        exit()

movies_df = load_data()

print(movies_df[movies_df['Genre'].str.contains('Crime', case=False, na=False)])

# List all unique genres
def list_genres(df):
    genres = set()
    for item in df['Genre'].dropna(): # get genre column
        for genre in item.split(','): # iterate through every genre
            genres.add(genre.strip()) 
    return sorted(genres)

genres = list_genres(movies_df)

# -------------------------------
# Recommend movies based on filters (genre, mood, rating)
# -------------------------------
def recommend_movies(genre=None, mood=None, rating=None, top_n=5):
    filtered_list = movies_df

    # creating a filtered movies list where genre and rating is user selected
    if genre:
        filtered_list = filtered_list[filtered_list['Genre'].str.contains(genre, case=False, na=False)]
    if rating:
        filtered_list = filtered_list[filtered_list['IMDB_Rating'] >= rating]

    # shuffles
    filtered_list = filtered_list.sample(frac=1).reset_index(drop=True)  # Randomize the order

    recommendations = []
    for idx, row in filtered_list.iterrows():
        overview = row['Overview']
        if pd.isna(overview):
            continue
        
        # computer sentiment polarity of movie based on overview
        polarity = TextBlob(overview).sentiment.polarity

        # if mood is negative and movie's polarity is positive or neutral
        if (mood and ((TextBlob(mood).sentiment.polarity < 0 and polarity > 0) or polarity >= 0)) or not mood:
            recommendations.append((row['Series_Title'], polarity))

        if len(recommendations) == top_n:
            break

    return recommendations if recommendations else "No suitable movie recommendations found."

# -------------------------------
# Display recommendations
# -------------------------------
def display_recommendations(recs, name):
    print(Fore.YELLOW + f"\n🎬 AI-Analyzed Movie Recommendations for {name}:")
    for idx, (title, polarity) in enumerate(recs, start=1):
        sentiment = "Positive 😊" if polarity > 0 else "Negative 😞" if polarity < 0 else "Neutral 😐"
        print(f"{Fore.CYAN}{idx}. {title} (Polarity: {polarity:.2f}, {sentiment})")

# -------------------------------
# Small processing animation
# -------------------------------
def processing_animation():
    for _ in range(3):
        print(Fore.YELLOW + ".", end="", flush=True)
        time.sleep(0.5)

# -------------------------------
# Handle AI recommendation flow
# -------------------------------
def handle_ai(name):
    print(Fore.BLUE + "\n🔍 Let's find the perfect movie for you!\n")

    # Show genres in a single line
    print(Fore.GREEN + "Available Genres: ", end="")
    for idx, genre in enumerate(genres, 1):
        print(f"{Fore.CYAN}{idx}. {genre}", end=" | ")
    print()

    # Get genre input
    while True:
        genre_input = input(Fore.YELLOW + "\nEnter genre number or name: ").strip()
        if genre_input.isdigit() and 1 <= int(genre_input) <= len(genres):
            genre = genres[int(genre_input) - 1]
            break
        elif genre_input.title() in genres:
            genre = genre_input.title()
            break
        print(Fore.RED + "Invalid input. Try again.\n")

    # Get mood input
    mood = input(Fore.YELLOW + "How do you feel today? (Describe your mood): ").strip()

    # Processing animation while analyzing mood
    print(Fore.BLUE + "\nAnalyzing mood", end="", flush=True)
    processing_animation()
    polarity = TextBlob(mood).sentiment.polarity
    mood_desc = "positive 😊" if polarity > 0 else "negative 😞" if polarity < 0 else "neutral 😐"
    print(f"\n{Fore.GREEN}Your mood is {mood_desc} (Polarity: {polarity:.2f}).\n")

    # Get rating input
    while True:
        rating_input = input(Fore.YELLOW + "Enter minimum IMDB rating (7.6–9.3) or 'skip': ").strip()
        if rating_input.lower() == 'skip':
            rating = None
            break
        try:
            rating = float(rating_input)
            if 7.6 <= rating <= 9.3:
                break
            print(Fore.RED + "Rating out of range. Try again.\n")
        except ValueError:
            print(Fore.RED + "Invalid input. Try again.\n")

    # Processing animation while finding movies
    print(f"{Fore.BLUE}\nFinding movies for {name}", end="", flush=True)
    processing_animation()
    recs = recommend_movies(genre=genre, mood=mood, rating=rating, top_n=5)

    if isinstance(recs, str):
        print(Fore.RED + recs + "\n")
    else:
        display_recommendations(recs, name)

    # Ask if user wants more recommendations
    while True:
        action = input(Fore.YELLOW + "\nWould you like more recommendations? (yes/no): ").strip().lower()
        if action == 'no':
            print(Fore.GREEN + f"\nEnjoy your movie picks, {name}! 🎬🍿\n")
            break
        elif action == 'yes':
            recs = recommend_movies(genre=genre, mood=mood, rating=rating, top_n=5)
            if isinstance(recs, str):
                print(Fore.RED + recs + "\n")
            else:
                display_recommendations(recs, name)
        else:
            print(Fore.RED + "Invalid choice. Try again.\n")

# -------------------------------
# Main program
# -------------------------------
def main():
    print(Fore.BLUE + "🎥 Welcome to your Personal Movie Recommendation Assistant! 🎥\n")
    name = input(Fore.YELLOW + "What's your name? ").strip()
    print(f"\n{Fore.GREEN}Great to meet you, {name}!\n")
    handle_ai(name)

if __name__ == "__main__":
    main()
