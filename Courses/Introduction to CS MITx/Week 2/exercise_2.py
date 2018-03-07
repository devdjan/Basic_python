# Task 1
x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while guess <= x: # Пока 0.0 меньше 25
    if abs(guess**2 - x) < epsilon: # (00^2 - 25) < 0.01 Переходим к else
        break # Выходим так как получается отриц число
    else: #
        guess += step # Увеличиваем переменную на 0.1 и так аж до 5 (4.99987 и тд.

if abs(guess**2 - x) >= epsilon: #
    print('failed') #
else: #
    print('succeeded: ' + str(guess)) #

print('------------------------------------')

# ----------------------

# Task 2
x1 = 25
epsilon1 = 0.01
step1 = 0.1
guess1 = 0.0

while guess1 <= x:
    if abs(guess1**2 - x) >= epsilon1:
        guess += step1

if abs(guess**2 - x) >= epsilon1:
    print('failed')
    