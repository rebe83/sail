# Import functions from the numpy library
from numpy.random import choice, shuffle
from numpy import roll

# Number of digits in number to be guessed
numDigits = 3
# Max number of guesses allowed
guesses = 10

# Message to user
print('I am thinking of a {}-digit number. Try to guess what it is.\n'
      .format(numDigits))
print('Here are some clues:')
print('When I say:    That means:')
print('  Ehhh         One digit is correct but in the wrong position.')
print('  Mhmm         One digit is correct and in the right position.')
print('  Nope         No digit is correct.')
print('There are no repeated numDigits in the number.')
print('You have {} chances to guess the number.'.format(guesses))

# Selecting <numDigits> numbers at random from [0,10) without replacement
num = choice(10, size=numDigits, replace=False)

# If the zeroth number in the list is a 0,
if num[0] == 0:
    # use numpy.roll to move all elements in the list over by one
    # numpy.roll([0,1,2]) -> [1,2,0]
    num = roll(num, 1)

# Convert the list of numbers into a string for printing and comparison
numStr = ''.join(map(str, num))

# Counter for round number
counter = 1

# Loop until forced to stop
while True:
    # Print current guess number and ask for a guess from the user
    guessStr = input('Guess #{}: '.format(counter))

    # If length of guess is not equal to the number of digits asked for,
    if len(guessStr) != numDigits:
        # print error message and skip rest of loop
        print('Wrong number of digits. Try again!')
        continue

    # If guess is not a number,
    if not guessStr.isdigit():
        # print error message and skip rest of loop
        print('Not a number. Try again!')
        continue

    # Check if guess is correct
    if guessStr == numStr:
        print('You got it!')
        break

    # Create list to hold the clues given
    clues = []

    # For each loop over the guess
    for index, digit in enumerate(guessStr):
        # If digit equals the value of the same location in numStr,
        if digit == numStr[index]:
            # digit is in right place
            clues.append('Mhmm')
        # Else if digit is in the solution string at all,
        elif digit in numStr:
            # digit is partially correct
            clues.append('Ehhh')

    # Mix up the order of the clues
    shuffle(clues)

    # If there are no clues,
    if len(clues) == 0:
        print('Nope')
    else:
        # Print the clues seperated by spaces
        print(' '.join(clues))

    # Increment the counter
    counter += 1

    # Check if out of guesses
    if counter > guesses:
        print('You ran out of guesses. The answer was {}.'.format(numStr))
        break
