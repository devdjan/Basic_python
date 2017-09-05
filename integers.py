#Hello Kiryha
#At that file you will se some basic code
#1 task
a = 10
P = 4 * a
print(P)

#2 task
a = 3
S = a*a
print(S)

#3 task
a = 2
b = 1
S = a * b
P = 2*(a + b)
print(S,P)

#4 task
d = 13
Pi = 3.14
L = Pi * d
print(L)

#5 task
a = 4
V = a ** 3
S = 6 * (a ** 2)
print(V, S)

# Hello world ten times
print("Hello world "  * 10)

#Lists
a = [[1,2,3],[4,5,6]]
print(a[0])
b = a[0]
print(b)
#---------------
a = [[1,2,3,4,5],[6,7],[8,9,10]]
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=" ")
        print()
#---------------
#Переменная цикла фор в питоне перебирает любіе єлементы
#Любой последовательности
a = [[1,2],[2,3,4],[4,5,6,7]]
for row in a:
    # for elem in row:
        print(row)
        print()
#---------------
#Попробую с помощью первого цикла перебрать номер стоки
#С помощью второго пробежаться по элементам внутри строки
a = [[1,2],[2,3,4],[5,6,7],[8,9]]
for row in a:
    for elem in row:
        print(elem, end=" ")
        print()
#---------------
#Вывод одной строки с помощью метода join
for row in a:
    print(' '.join([str(elem) for elem in row]))

#-----------------------------------------------------
# Tasks from task.txt
#-----------------------------------------------------

# At that part examples from tasks.txt
#Define triangle. And decide exist it or not?
a = 3
b = 7
c = 9
def triangle (a,b,c):
    if (a < b + c) or (b < c + a) or (c < a + b):
        return true
    else:
        return false
#or change return for "Print (Triangle exist) etc."

#Write an function wich creates and initialises matrix. Entry  - m,n,k
#m, n height and width. K - element wich will be initialising the matrix.

#Testing,  i want to know how built matrix, before start




