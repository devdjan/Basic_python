# Simple algorithm
# I will use use to improve task with guesses.
# Firstly i tried simple while loop
# then bisection search(dividing the area of guesses)
# Now it is time for newton-raphson
epsilon = 0.01
y = 36
guess = y / 2.0
numGuesses = 0

while abs(guess*guess - y) > epsilon:
    numGuesses += 1
    guess = (guess - ((guess**2)- y) / (2 * guess))
# what we do       5        1   2    4    3
# If someone wants to calculate it manually.

print('Num of guesses = ' + str(numGuesses))
print('Square root of ' + str(y) + ' is, about ' + str(guess))
