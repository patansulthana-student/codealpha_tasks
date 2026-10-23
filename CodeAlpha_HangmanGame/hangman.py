
import random

# Step 1: Store five predefined words
words = ["PYTHON", "COMPUTER", "CODING", "PROGRAM", "DEVELOPER"]

# Step 2: Select one random word
secret_word = random.choice(words)

# Step 3: Create a list for guessed letters
guessed_letters = []

# Step 4: Set the maximum incorrect guesses
max_wrong_guesses = 6
wrong_guesses = 0

print("===== WELCOME TO HANGMAN =====")
print("Guess the word one letter at a time!")
print("You can make a maximum of 6 incorrect guesses.")

# Step 5: Continue until the player wins or loses
while wrong_guesses < max_wrong_guesses:

    # Step 6: Display hidden letters
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Incorrect guesses left:", max_wrong_guesses - wrong_guesses)

    # Step 7: Check if the player has won
    if all(letter in guessed_letters for letter in secret_word):
        print("Congratulations! You guessed the word:", secret_word)
        break

    # Step 8: Get a letter from the player
    guess = input("Enter one letter: ").strip().upper()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Step 9: Check repeated guesses
    if guess in guessed_letters:
        print("You already guessed that letter. Try another.")
        continue

    guessed_letters.append(guess)

    # Step 10: Check whether the letter is correct
    if guess in secret_word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")

else:
    print("\nGame over! You ran out of guesses.")
    print("The correct word was:", secret_word)
