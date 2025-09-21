"""
Have a look at the script called 'human-guess-a-number.py' (in the same folder as this one).

Your task is to invert it: You should think of a number between 1 and 100, and the computer 
should be programmed to keep guessing at it until it finds the number you are thinking of.

At every step, add comments reflecting the logic of what the particular line of code is (supposed 
to be) doing. 
"""

def check_char(s):
    """ Check if string 's' represents an expected character. """
    return s == 'g' or s == 's' or s == 'y'

def input_integer(prompt):
    """ Asks user for an integer input. If valid, the string input is returned as an integer. """
    guess = input(prompt) # Ask the user for their guess
    while not check_char(guess): # Repeat until the user inputs a valid integer
        print('Please, enter "g", "s" ot "y"')
        guess = input(prompt)  
    return guess

print("Think about a number between 1 and 100. I'll try to find it!")

#those are the bondaries between which the number is known to be. Due to rounding after division, max_guessed = max - 1
max = 101
min = 0

#initial guess at the center of distribution
guess = 50
answer = input_integer("Is it 50? Type g if your number is greater, s if it is smaller and y if I found it\n")

while answer != 'y': # Repeat until I win.
    
    #boundaries are updated
    if answer == 'g':
        min = guess
    else:
        max = guess

    #new guess is always halfway between the boundaries
    guess = (max+min)//2
    answer = input_integer(f"Is it {guess}?\n")

print("I'm the best.")