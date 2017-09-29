import stdio
import stdarray
import random
# Start doing task from books/ Added stdio library, to
# use some code from book;
n = 4
a = [] #initializing empty array
for i in range(n):
    a += [0.0] # adding one elem in the end of array

# Some fundamental operations
# a = [1,2,3,4,5]
# total = 0.0
# for i in range(len(a)):
#     total += a
# average = total / len(a)
# print(average)

# Перебор элементов массива не обращаясь к индексам явно.
# Поместим имя массива после ключевого слова in в операторе for
total = 0.0
for v in a:
    total += v
average = total / len(a)
stdio.writeln(average)

# Написать функцию вычисляющую среднее значение массива
# a = [1,2,3,4,0,-1]
# total = 0
# for i in a:
#     total = total + a
#     aver = total / len(a)


# Alias
# aliasing. Когда две переменные ссылаются на один и тот же объект
x = [1,3,4,0,90,905]
y = [6,4,21,4345,2]
x = y
print(y)


#----------------------------------------------------------
# ИГРА В КАРТЫ
#----------------------------------------------------------
SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
RANKS = ['2', '3', '4', '5', '6', '7','8','9','10', 'Jack', 'Queen', 'King', 'Ace']

# rank = random.randrange(0, len(RANKS))
# suit = random.randrange(0, len(SUITS))
# stdio.writeln(RANKS[rank] + ' of ' + SUITS[suit])

# Иницализируем массив массив длиной 52 представляющего колоду карт,
# используя лва только что определенных массива
deck = []
for rank in RANKS:
    for suit in SUITS:
        card = rank + ' of ' + suit
        deck += [card] # Равносильно desk = desk + card ?)


# Обмен єлементов местами. Поменяем карті с индексами i и j
# Только изменим порядок элементов массива на обратный
# temp = deck[i]
# deck[i] = deck[j]
# deck[j] = temp
# Меняется порядок элементов в массиве, но не сам набор эл. в массиве
# Когда i и j  равны то массив не изменяется


# Перестановка колоды карт
n = len(deck)
for i in range(n):
    r = random.randrange(i, n)
    temp = deck[r]
    deck[r] = deck[i]
    deck[i] = temp
    print(temp)

#----------------------------------------------------------
# Выборка без замены
#----------------------------------------------------------
import random
import sys
import stdarray
import stdio

m = 11#
n = 120

# Инициализация одномерного массива
perm = stdarray.create1D(n, 0)
for i in range(n):
    perm[i] = i
# Случайная выборка м в предело до н
for i in range(m):
    r = random.randrange(i, n)

# Обмен массивов
temp = perm[r]
perm[r] = perm[i]
perm[i] = temp

# Вывод
for i in range(m):
    stdio.write(str(perm[i]) + ' ')
stdio.writeln()

#----------------------------------------------------------
# Модель коллекции купонов
#----------------------------------------------------------
# Получает число н, создает последовательность случайных
# целочисленных значений от 0 до н-1
# Значения - карточки. И мы хотим знать встречалась ли она прежде
# isCollected - массив в котором [индекс] = значению
# т.е isCollected[i] - True если встретится карточка со значением i
# False - в противном случае

import random
import sys
import stdarray
import stdio

n = 5
count = 0  # Кол-во собранных купонов
collectedCount = 0 # Количество "различных" собранных купонов
# isCollected[i] - Проверяем есть ли уже купон i ?
# value - значение текущего купона

isCollected = stdarray.create1D(n, False)
# Проверяем
while (collectedCount < n):
    value = random.randrange(0, n)
    count += 1

if not isCollected[value]:
    collectedCount += 1
    isCollected[value] = True
stdio.writeln(count)

#----------------------------------------------------------
# Решето Эратосфена
#----------------------------------------------------------
import stdarray
import stdio

n = 10 # Аргумент
isPrime = stdarray.create1D(n+1, True) #

for i in range(2, n):
    if(isPrime[i]):
        for j in range(2, n//i + 1):
            isPrime[i * j] = False
# Подсчет простых чисел
count = 0
for i in range(2, n+1):
    if (isPrime[i]):
        count += 1
stdio.write(count)






#----------------------------------------------------------
#Write a Python program to create an array of 5 integers
# and display the array items.
# Access individual element through indexes
# a = [1,4,5,6,7]
# for i in range(a):
#     print(i)
#     print(i[-1])
array = [1,4,5,6,7]
for i in array:
    print(i)
    print(array[1]) # five times 4 4 4 4 4

#----------------------------------------------------------
#Write a Python program to append a new item to the end of the array.
array = [1,2,3,4,5,0]
array.append(6)
print(array)

#----------------------------------------------------------
#Write a Python program to reverse the order of the items in the array.
#Maybe using .reverse

array = [1,2,3,6,7,8,0,-1]
array.reverse()
print(array)

#Tomorrov i will try to write some function of "reverse"
# Cheto ne vishlo(
# Я бы взял [-1] массива в с помощью функции по аналогии с append, только
# наоборот, записал бы в другой список

#----------------------------------------------------------
#Write a Python program to get the length in bytes of one array item in the internal representation.
# array = [0,1,34,-1,3]
# array.itemsize
# print(array)

#----------------------------------------------------------
# in bytes
def byte_size(byte):
    return len(byte.encode('utf-8'))


#----------------------------------------------------------
# Stack overflow solution using sys library
import sys
# array_test = [1,2,3,-1]
# getsizeof[1,23,4]
# print(array_test)

#----------------------------------------------------------
# Write a Python program to append items from inerrable to the end of the array.
test = [1,2,3,4,5,6]
# Может воспользоваться методом extended
def append_items(test):
    return append_items().extend

#----------------------------------------------------------
# Convert an array to an array of machine values and return the bytes representation
# Не понял как сделать, гуглил. Есть только варианты с помощью библиотек(

