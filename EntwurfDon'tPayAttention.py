# import random
#
# with open('Words_Lib.txt', 'r') as file:
#     words_library = file.read().splitlines() #I know that this library makes this program to heavy, but it works as it should work :)
#
# hidden_word = random.choice(words_library) #
# print(hidden_word)
#
# def instruct_user(): #only instructions, nothing special
#     print("You have to guess a word that contains 5 letters from the library. You have 6 attempts to guess the word.")
#     print("If you guess the word correctly, you win! If you dont, you lose! ")
#     print("If the letter on the second or next attempt is gray, that means does the hidden word doesn't contain this character.")
#     print("If the letter on the second or next attempt is yellow, that means does the hidden word does contain this character, but in a different position.")
#     print("If the letter on the second or next attempt is green, that means the hidden word contains this character, and it's in the correct position.")
#     print("Good luck!")
#     print("----------------------------------------")
#
# def validate_word(word): #word validation
#     if len(word) != 5:
#         return False
#     elif not word.isalpha():
#         return False
#     else:
#         return True
#
# def check_word(word): #checking whether word exist in library
#     if word in words_library:
#         return True
#     else:
#         return False
#
# def check_guess(guess):
#     if guess == hidden_word:
#         return True
#     else:
#         return False
#
# def check_letter(some):
#     for i, char in enumerate(some):
#         if char in hidden_word:
#             if char == hidden_word[i]:
#                 print("\033[92m" + char + "\033[0m", end='')
#             else:
#                 print("\033[93m" + char + "\033[0m", end='')
#         else:
#             print(f"{char}", end='')
#     print("")
#
#
# print("Welcome to the Wordle game!")
# pointer = 0
#
#
#
#
# while True:
#     try:
#         pointer += 1
#         attempts_left = 6 - pointer
#         attempt = input("Guess the word that contains 5 letters (type 'i' to see the instructions): ").lower().strip()
#         validation = validate_word(attempt)
#         in_lib = check_word(attempt)
#         right_word = check_guess(attempt)
#         if attempt == 'i':
#             instruct_user()
#             pointer -= 1
#             continue
#         if not validation:
#             attempts_left = 6 - pointer + 1 #here works something bad. Pointer doesn't work correctly. this Kostyl' works.
#             pointer -=1
#             print(f"Please try again and follow the instructions! Attempts left: {attempts_left}.")
#             continue
#         elif not in_lib:
#             print(f"This word doesn't exist! Please try again! Attempts left: {attempts_left}.")
#             pointer -=1
#             continue
#         else:
#             if right_word:
#                 check_letter(attempt)
#                 print("Congratulations! You guessed the word correctly!")
#                 break
#             elif attempts_left != 0:
#                 check_letter(attempt)
#                 print(f"Sorry, you didn't guess the word correctly! Try again! Attempts left: {attempts_left}.")
#             else:
#                 print("-----------------------------------------------------------------------------------------")
#                 print("Sorry, you didn't guess the word correctly! You lost! The word was: ", hidden_word)
#                 exit()
#     except KeyboardInterrupt or ValueError:
#         print(f"\nPlease enter a valid data and start the Program again!")
#         exit()