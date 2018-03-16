# For details look into exercise_3
# Bisection search Cube root example
cube = 27
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
# Суть в чем?
# Мы постоянно отсеиваем большие значения
# Приближаясь к тому числу, которое у в КУБЕ даст нам Cube
# Пример: Вот есть у нас куб = 27 . В начале мы проверяем
# модуль( 27**3 - куб(23)) < куб(27) - конечно меньше. Увеличиваем счетчик на 1
# Если попытка(quess = 13.5) ** 3 < 27 - меньшему == попытку. Но 13**3 > cube, идем дальше
# В противном случае:
# Приравниваем высокому значению == попытку. Тем самым отсеивая половину. Т.к. high = 27 стало high = 13.5
# И так мі продолжаем до тех пор разбивать, пока у нас quess +- не буе=дет равно кубу
# Выводим кол-во попыток и число близкое к кубу