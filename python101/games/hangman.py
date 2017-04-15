# Function to clear screen
def clearScreen():
    print('\n' * 100)


# Function to draw man based on number of incorrect guesses
def draw_man(incorrectGuesses):
    if incorrectGuesses == 0:
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('____________')
    elif incorrectGuesses == 1:
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('-----')
        print('____________')
    elif incorrectGuesses == 2:
        print('')
        print('  |')
        print('  |')
        print('  |')
        print('  |')
        print('  |')
        print('  |')
        print('-----')
        print('____________')
    elif incorrectGuesses == 3:
        print('  ______')
        print('  |')
        print('  |')
        print('  |')
        print('  |')
        print('  |')
        print('  |')
        print('-----')
        print('____________')
    elif incorrectGuesses == 4:
        print('  ______')
        print('  |    |')
        print('  |')
        print('  |')
        print('  |')
        print('  |')
        print('  |')
        print('-----')
        print('____________')
    elif incorrectGuesses == 5:
        print('  ______')
        print('  |    |')
        print('  |    O')
        print('  |')
        print('  |')
        print('  |')
        print('  |')
        print('-----')
        print('____________')
    elif incorrectGuesses == 6:
        print('  ______')
        print('  |    |')
        print('  |    O')
        print('  |    |')
        print('  |    |')
        print('  |')
        print('  |')
        print('-----')
        print('____________')
    elif incorrectGuesses == 7:
        print('  ______')
        print('  |    |')
        print('  |    O')
        print('  |   /|')
        print('  |    |')
        print('  |')
        print('  |')
        print('-----')
        print('____________')
    elif incorrectGuesses == 8:
        print('  ______')
        print('  |    |')
        print('  |    O')
        print('  |   /|\\')
        print('  |    |')
        print('  |')
        print('  |')
        print('-----')
        print('____________')
    elif incorrectGuesses == 9:
        print('  ______')
        print('  |    |')
        print('  |    O')
        print('  |   /|\\')
        print('  |    |')
        print('  |   /')
        print('  |')
        print('-----')
        print('____________')
    elif incorrectGuesses == 10:
        print('  ______')
        print('  |    |')
        print('  |    O')
        print('  |   /|\\')
        print('  |    |')
        print('  |   / \\')
        print('  |')
        print('-----')
        print('____________')


# Ask for the word that is to be guessed and convert is to lower case
clearScreen()
answer = list(input('Enter a word or phrase to guess: ').lower())
clearScreen()

# Initialize number of incorrect guesses
numIncorrect = 0

# Initialize list of letters that have been guessed
guessedLetters = []

# Initialize the target word/phrase in spaces and hyphens
guess = [' ' if char == ' ' else '-' for char in answer]

# Print blank man and the blank guess
draw_man(numIncorrect)
print(''.join(guess))

while True:
    # Convert list to string and print letters already guessed
    print('Guessed letters:', ' '.join(guessedLetters))

    # Ask for a letter
    letter = input('Guess a letter: ')
    clearScreen()

    # If more than one letter entered
    if len(letter) != 1:
        print('Please enter a single letter.')

    # If letter already guessed
    elif letter in guessedLetters:
        print('You already guessed that letter, try again.')

    # If letter in answer
    elif letter in answer:
        print('Good guess!')
        for index, value in enumerate(answer):
            if value == letter:
                guess[index] = letter
        guessedLetters.append(letter)

    else:
        print('WRONG guess.')
        numIncorrect += 1
        guessedLetters.append(letter)

    draw_man(numIncorrect)
    print(''.join(guess))

    if numIncorrect == 10:
        print("You're DEAD!")
        break

    if '-' not in guess:
        print('Success! You LIVE!')
        break
