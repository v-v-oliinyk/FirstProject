import random

with open('Words_Lib.txt', 'r') as file:
    words_library = file.read().splitlines() #I know that this library makes this program to heavy, but it works as it should work :)

hidden_word = random.choice(words_library).lower()
print(hidden_word)

def instruct_user(): #only instructions, nothing special
    print("You have to guess a word that contains 5 letters from the library. You have 6 attempts to guess the word.")
    print("If you guess the word correctly, you win! If you don`t, you lose! ")
    print("If the letter on the second or next attempt is gray, that means does the hidden word doesn't contain this character.")
    print("If the letter on the second or next attempt is yellow, that means does the hidden word does contain this character, but in a different position.")
    print("If the letter on the second or next attempt is green, that means the hidden word contains this character, and it's in the correct position.")
    print("Good luck!")
    print("----------------------------------------")

def validate_word(word): #word validation
    if len(word) != 5:
        return False
    elif not word.isalpha():
        return False
    else:
        return True

def check_word_in_library(word): #checks whether word exist in library
    if word in words_library:
        return True
    else:
        return False

def check_guess(guess): #checks whether current word is a secret word.
    if guess == hidden_word:
        return True
    else:
        return False

def check_letter(some): #checks letters in word
    for i, char in enumerate(some):
        if char in hidden_word:
            if char == hidden_word[i]:
                print("\033[92m" + char + "\033[0m", end='')
            else:
                print("\033[93m" + char + "\033[0m", end='')
        else:
            print("\033[0m" + char + "\033[0m", end='') #\033[90m for gray. But I didn't like it.
    print("")


print("Welcome to the Wordle game!")
pointer = 0


while True:
    try:
        attempt = input("Guess the word that contains 5 letters (type 'i' to see the instructions): ").lower().strip()

        if attempt == 'i': #shows instructions if needed
            instruct_user()
            continue

        correctness = check_guess(attempt)

        if not validate_word(attempt):
            print(f"Please try again and follow the instructions! Attempts left: {6 - pointer}.")
            continue
        if not check_word_in_library(attempt):
            print(f"This word doesn't exist! Please try again! Attempts left: {6 - pointer}.")
            continue

        pointer += 1
        attempts_left = 6 - pointer

        if correctness:
            check_letter(attempt)
            print("Congratulations! You guessed the word correctly!")
            break
        elif attempts_left > 0:
            check_letter(attempt)
            print(f"Sorry, you didn't guess the word correctly! Try again! Attempts left: {attempts_left}.")
        else:
            print("-----------------------------------------------------------------------------------------")
            print("Sorry, you didn't guess the word correctly! You lost! The word was: ", hidden_word)
            exit()
    except KeyboardInterrupt or ValueError:
        print(f"\nPlease enter a valid data and start the Program again!")
        exit()



