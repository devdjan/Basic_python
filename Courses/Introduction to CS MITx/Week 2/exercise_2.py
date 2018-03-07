# Task 1
x = 25
epsilon = 0.01
step = 0.1
guess = 5

while guess <= x: # Пока 0.0 меньше 25
    if abs(guess**2 - x) < epsilon: # (00^2 - 25) < 0.01 Переходим к else
        break # Выходим так как по МОДУЛЮ число никак не меньше epsilo
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
guess1 = 0.1

while guess1 <= x1:
    if abs(guess1**2 - x1) >= epsilon1:
        guess1 += step1

if abs(guess**2 - x1) >= epsilon1:
    print('failed')
else:
    print('succeeded: ' + str(guess1))

print('------------------------------------')

# ----------------------

# Task 3
x2 = 25
epsilon2 = 0.01
step2 = 0.1
guess2 = 0.0

while abs(guess2**2 - x2) >= epsilon2:
    if guess2 <= x2:
        guess2 += step2
    else:
        break

if abs(guess2**2 - x2) >= epsilon2:
    print('failed')
else:
    print('succeeded: ' + str(guess2))
