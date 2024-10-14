# Import shuffle from random
from random import shuffle

# Create initial list with "ball" in the middle
mylist = [' ', 'O', ' ']

# Make shuffle list function


def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

# Make player guess function


def player_guess():
    guess = ''
    # Will loop through if the user does not enter 1, 2, or 3
    while guess not in ['0', '1', '2']:
        guess = input("Pick a number: 0, 1, or 2")
    # Guess needs to convert to int because it will be used as an index
    return int(guess)

# Make check guess function


def check_guess(mylist, guess):
    if mylist[guess] == 'O':
        print("Correct!")
    else:
        print("Wrong guess")
        print(mylist)

# Functions interact here


mixedup_list = shuffle_list(mylist)
guess = player_guess()
check_guess(mixedup_list, guess)
