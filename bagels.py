from numpy.random import choice, shuffle
from numpy import roll

digits = 3
guesses = 10

print('I am thinking of a {}-digit number. Try to guess what it is.'
      .format(digits))
print('Here are some clues:')
print('When I say:    That means:')
print('  Ehhh         One digit is correct but in the wrong position.')
print('  Mhmm         One digit is correct and in the right position.')
print('  Nope         No digit is correct.')
print('There are no repeated digits in the number.')
print('You have {} chances to guess the number.'.format(guesses))

# Create a random number.
num = choice(10, size=digits, replace=False)
if num[0] == 0:
    num = roll(num, 1)
numStr = ''.join(map(str, num))

counter = 1

while True:
    guess = input('Guess #{}: '.format(counter))

    if len(guess) != digits:
        print('Wrong num of digits. Try again!')
        continue

    if not guess.isdigit():
        print('That is not a num. Try again!')
        continue

    # Create the clues.

    clues = []

    for pos in range(digits):
        if int(guess[pos]) == num[pos]:
            clues.append('Mhmm')
        elif int(guess[pos]) in num:
            clues.append('Ehhh')

    shuffle(clues)

    if len(clues) == 0:
        print('Nope')
    else:
        print(' '.join(clues))

    counter += 1

    if guess == numStr:
        print('You got it!')
        break

    if counter > guesses:
        print('You ran out of guesses. The answer was {}.'.format(numStr))
        break
