import random
import settings
import sys

word_list = ["apple", "banana", "orange", "grape", "kiwi"]
secret_word = random.choice(word_list)
if settings.debug_Mode:
    print(secret_word)

guessed_letters = []
word_completion = ["_"] * len(secret_word)

def play_game(input_func):
    while settings.guesses_left > 0 and "_" in word_completion:
        print(" ".join(word_completion))
        print("guess a letter")
        guess = input_func().strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        guessed_letters.append(guess)
        if guess in secret_word:
            for index in range(len(secret_word)):
                if secret_word[index] == guess:
                    word_completion[index] = guess
        else:
            settings.guesses_left -= 1
        print(f"Guesses left: {settings.guesses_left}")

    if "_" not in word_completion:
        print(f"Congratulations, you guessed the word: {secret_word}!")
    else:
        print(f"You ran out of guesses. The word was: {secret_word}")

if __name__ == "__main__":
    play_game(lambda: sys.stdin.readline())