def clearScreen():
    print('\n' * 100)


def draw_man(guess_count):
    if guess_count == 0:
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
    elif guess_count == 1:
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('-----')
    elif guess_count == 2:
        print('')
        print('  |')
        print('  |')
        print('  |')
        print('  |')
        print('  |')
        print('  |')
        print('-----')
    elif guess_count == 3:
        print('  ______')
        print('  |')
        print('  |')
        print('  |')
        print('  |')
        print('  |')
        print('  |')
        print('-----')
    elif guess_count == 4:
        print('  ______')
        print('  |    |')
        print('  |')
        print('  |')
        print('  |')
        print('  |')
        print('  |')
        print('-----')
    elif guess_count == 5:
        print('  ______')
        print('  |    |')
        print('  |    O')
        print('  |')
        print('  |')
        print('  |')
        print('  |')
        print('-----')
    elif guess_count == 6:
        print('  ______')
        print('  |    |')
        print('  |    O')
        print('  |    |')
        print('  |    |')
        print('  |')
        print('  |')
        print('-----')
    elif guess_count == 7:
        print('  ______')
        print('  |    |')
        print('  |    O')
        print('  |   /|')
        print('  |    |')
        print('  |')
        print('  |')
        print('-----')
    elif guess_count == 8:
        print('  ______')
        print('  |    |')
        print('  |    O')
        print('  |   /|\\')
        print('  |    |')
        print('  |')
        print('  |')
        print('-----')
    elif guess_count == 9:
        print('  ______')
        print('  |    |')
        print('  |    O')
        print('  |   /|\\')
        print('  |    |')
        print('  |   /')
        print('  |')
        print('-----')
    elif guess_count == 10:
        print('  ______')
        print('  |    |')
        print('  |    O')
        print('  |   /|\\')
        print('  |    |')
        print('  |   / \\')
        print('  |')
        print('-----')


clearScreen()

print('Enter a word or phrase to guess:')
answer = list(input())

clearScreen()

wrong_guesses = 0
guess = [' ' if char == ' ' else '_' for char in answer]
guessed_letters = []

draw_man(wrong_guesses)
print(''.join(guess))

while True:

    guessed_letters.sort()
    print('Guessed letters:', ' '.join(guessed_letters))
    print('Guess a letter:')
    letter = input()

    clearScreen()

    if letter == 'quit':
        break
    if len(letter) != 1:
        print('Please enter a single letter.')

    elif letter in guessed_letters:
        print('You already guessed that letter, try again.')

    elif letter in answer:
        print('Good guess!')
        for index in range(len(answer)):
            if answer[index] == letter:
                guess[index] = letter
        guessed_letters.append(letter)

    else:
        print('WRONG guess.')
        wrong_guesses += 1
        guessed_letters.append(letter)

    draw_man(wrong_guesses)
    print(''.join(guess))

    if wrong_guesses == 10:
        print("You're DEAD!")
        break

    if '_' not in guess:
        print('Success! You LIVE!')
        break
