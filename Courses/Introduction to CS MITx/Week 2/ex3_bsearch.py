# For details look into exercise_3
# Bisection search Cube root example
cube = 54
epsilon = 0.01
numGuesses = 0
low = 0.0
high = cube
quess = (high + low) / 2.0

while abs(quess**3 - cube) >= epsilon:  #
    print('low = ' + str(low) + ' high = ' + str(high) + ' quess = ' + str(quess))
    numGuesses += 1
    if quess**3 < cube:
        low = quess
    else:
        high = quess
    quess = (high + low) / 2.0
print('numGuesses = ' + str(numGuesses))
print(str(quess) + ' is close to cube root of ' + str(cube))

