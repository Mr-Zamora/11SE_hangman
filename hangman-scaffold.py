import random

# Game settings
# Maximum score the player can have - they lose if it reaches 0
MAX_SCORE = 100
# Number of wrong guesses before a hint is offered
HINT_THRESHOLD = 3

# Built-in word lists organized by difficulty level
# Each difficulty has its own list of words that can be randomly chosen for the game
DIFFICULTY_WORDS = {
    "easy": ["apple", "grape", "peach", "chair", "table"],
    "medium": ["picture", "blanket", "journey", "horizon"],
    "hard": ["complexity", "instrument", "revolutionary"]
}

def display_word(word, guessed_letters):
    """
    Shows the word with guessed letters revealed and unguessed letters as underscores
    Example: If word is "apple" and guessed letters are "a" and "p", shows: "a p p _ _"
    """
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def get_hint(word, guessed_letters):
    """
    Provides a hint by randomly selecting one of the unguessed letters in the word
    Returns None if all letters have been guessed
    """
    # Create a list of letters that haven't been guessed yet
    missing = [letter for letter in word if letter not in guessed_letters]
    return random.choice(missing) if missing else None

def main_menu():
    """
    Displays the main game menu and handles player choices
    """
    print("\nWelcome to Hangman!")
    while True:
        print("\n1. Play Game\n2. Exit")
        choice = input("Choose option: ").strip()
        if choice == "1":
            start_game()
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1 or 2")

def start_game():
    """
    Main game logic that:
    1. Lets player choose difficulty
    2. Picks a random word
    3. Manages the game loop for guessing letters
    4. Tracks score and provides hints when needed
    """
    # Difficulty selection loop - keeps asking until valid choice is made
    while True:
        difficulty = input("\nChoose difficulty (easy/medium/hard): ").lower()
        if difficulty in DIFFICULTY_WORDS:
            break
        print("Invalid difficulty! Please choose easy/medium/hard")
    
    # Game setup
    current_word = random.choice(DIFFICULTY_WORDS[difficulty]).lower()
    guessed_letters = set()  # Using a set to store unique guessed letters
    score = MAX_SCORE
    incorrect_guesses = 0
    hint_used = False
    
    while True:
        # Show current game state to the player
        print(f"\nCurrent word: {display_word(current_word, guessed_letters)}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
        print(f"Score: {score}")

        guess = input("Guess a letter or the whole word: ").lower().strip()

        # Handle full word guesses - gives bonus points for correct guess
        if guess == current_word:
            score += 10
            print(f"\nCongratulations! You guessed the word: {current_word}")
            print(f"Final Score: {score}")
            return

        # Handle single letter guesses
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed that letter!")
                continue
                
            guessed_letters.add(guess)
            
            if guess in current_word:
                score += 10
                print(f"Correct! +10 points (Current score: {score})")
            else:
                score -= 10
                incorrect_guesses += 1
                print(f"Wrong guess! -10 points (Current score: {score})")
        else:
            print("Invalid input! Please enter a single letter or the full word.")
            score -= 10
            incorrect_guesses += 1

        # Check if player has won by revealing all letters
        if all(letter in guessed_letters for letter in current_word):
            score += 10
            print(f"\nCongratulations! You guessed the word: {current_word}")
            print(f"Final Score: {score}")
            return

        # Offer hint after certain number of incorrect guesses
        if incorrect_guesses >= HINT_THRESHOLD and not hint_used:
            if hint := get_hint(current_word, guessed_letters):
                print(f"\nHint: The letter '{hint}' is in the word!")
                hint_used = True

        # Check if player has lost by running out of points
        if score <= 0:
            print("\nYou scored 0 points. Game over!")
            print(f"The word was: {current_word}")
            return

if __name__ == "__main__":
    main_menu()