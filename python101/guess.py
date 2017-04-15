from numpy.random import randint

start = 0
end = 100
value = randint(start, end)

print("I'm thinking of a number between {} and {}.".format(start, end))

guess = -1
counter = 0
while guess != value:
    guessStr = input('Guess the number: ')
    if not guessStr.isdigit():
        print('Whoops! Make sure input is a number in the range specified')
        continue

    guess = int(guessStr)

    if guess < value:
        print('Higher.')
    elif guess > value:
        print('Lower.')
    counter += 1

print('Congratulations! You got it! Tries needed:', counter)
