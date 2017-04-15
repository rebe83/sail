import matplotlib.pyplot as plt
from numpy import zeros
from numpy import mean
from numpy.random import randint

bestGuess = lambda a, b: (b + a) // 2
N = int(input('Number of Trials:'))
counter = zeros(N)
for i in range(N):
    start, end = 0, 100
    value = randint(start, end)
    while True:
        guess = bestGuess(start, end)
        if guess == value:
            break
        elif guess < value:
            start = guess
        elif guess > value:
            end = guess
        counter[i] += 1

print(counter)

plt.plot(counter)
plt.xlabel('Trial Number')
plt.ylabel('Number of Attempts Needed')
plt.axhline(mean(counter), color='r', label='Mean Tries')
plt.title('Simulation of Number Guessing Game')
plt.legend()

plt.figure()
plt.hist(counter, bins=[0, 1, 2, 3, 4, 5, 6, 7], align='left', edgecolor='k')
plt.xlabel('Number of Attempts Needed')
plt.ylabel('Number of Trials')
plt.title('Histogram of Number Guessing Game Simulation')
plt.show()
