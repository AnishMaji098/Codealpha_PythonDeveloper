import random

# Five predefined words for the game
WORDS = ["python", "computer", "hangman", "program", "keyboard"]
MAX_WRONG_GUESSES = 6


def display_word(secret_word, guessed_letters):
    """Show guessed letters and hide the letters that have not been guessed."""
    return " ".join(
        letter if letter in guessed_letters else "_"
        for letter in secret_word
    )


def play_game():
    secret_word = random.choice(WORDS)
    guessed_letters = []
    wrong_guesses = 0

    print("\n===== WELCOME TO HANGMAN =====")
    print("Guess the hidden word one letter at a time.")
    print(f"You can make up to {MAX_WRONG_GUESSES} incorrect guesses.\n")

    while wrong_guesses < MAX_WRONG_GUESSES:
        print("Word:", display_word(secret_word, guessed_letters))
        print("Incorrect guesses:", wrong_guesses, "/", MAX_WRONG_GUESSES)

        if guessed_letters:
            print("Guessed letters:", ", ".join(sorted(guessed_letters)))

        guess = input("Enter a letter: ").lower().strip()

        # Validate the player's input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter exactly one alphabetic letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.\n")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("Correct guess!\n")
        else:
            wrong_guesses += 1
            print("Sorry, that letter is not in the word.\n")

        # Check whether every letter has been guessed
        if all(letter in guessed_letters for letter in secret_word):
            print("Word:", display_word(secret_word, guessed_letters))
            print("\nCongratulations! You guessed the word:", secret_word)
            break
    else:
        print("Game over! You used all 6 incorrect guesses.")
        print("The correct word was:", secret_word)


def main():
    while True:
        play_game()
        play_again = input("\nWould you like to play again? (y/n): ").lower().strip()

        if play_again != "y":
            print("\nThanks for playing Hangman. Goodbye!")
            break


if __name__ == "__main__":
    main()
