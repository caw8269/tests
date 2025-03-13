#import modules and other files that are used
import random
import settings

#define a secret word from a list
word_list = ["apple", "banana", "orange","grape", "kiwi"]
secret_word = random.choice(word_list)
if settings.debug_Mode:
    print(secret_word)

#define some variables
guessed_letters = []
word_completion = ["_"] * len(secret_word)

#game loop
while settings.guesses_left > 0 and "_" in word_completion:
    #display the current state of the word
    print(" ".join(word_completion))
    #get the players guess
    guess = input("Guess a letter: ").lower()
    #check if the guess is valid
    if len(guess) !=1 or not guess.isalpha():
        print("Please enter a single letter")
        continue
    #if the guess has already been made
    if guess in guessed_letters:
        print("you already guessed that letter")
        continue
    #update guessd letters
    guessed_letters.append(guess)
