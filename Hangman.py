# This will be one of my masterpieces in programming, if perfected.

# Created by Zur-en-Arrh

import random  # Useful to select a topic from the file.

# Functions


def same_letter(user_letter, word_to_guess):
    if user_letter == word_to_guess:

        return True
    else:
    return False


def wrong_guess(prevdisp, currdisp):
    if prevdisp == currdisp:
        return True
    else:
        return False


# Dealing with the file.
filename = input("Which file do you want to play with ")
topics = str(open(filename, 'r').read())
list_of_topics = topics.split()  # This is the list that contains the topics randomly selected from the file.
guess_me = list(list_of_topics[random.randint(0, len(list_of_topics) - 1)]) # This is what the user will need to figure out.

# Printing out the Dashes for the user.
disp = []
for i in range(0, len(guess_me)):
    disp.append("_")

# This is just the declaration of the number of wrong guesses. This'll always be 0 at the start of the game.
wrong_guesses = 0

# While loop for game. Also note in hangman, you're only allowed 5 wrong guesses till the body is complete.
while wrong_guesses < 6:
    print(' '.join(disp))  # Prints the game in an acceptable format to the user.
    predisp = disp[:]
    if disp == guess_me:  # end the game when the user wins.
        break
    user_guess = str(input("Which letter do you think will there be? ")).lower()  # if the user enters capital letters.


    for i in range(len(guess_me)):
        if same_letter(user_guess, guess_me[i]):
            disp[i] = user_guess
    if wrong_guess(predisp, disp):
        wrong_guesses += 1
    print("You have ", 6 - wrong_guesses, "guess/es remaining")  # Show the user how many tries he has left.
    if wrong_guesses == 6:
        print("You got hung! Better luck next time")
        print("The movie is: ")
        print(' '.join(guess_me))
        break

if wrong_guesses < 6:
    print("Well Done you won the game!")

# Code is now working absolutely fine. Extend the game to incorporate files of any type.
