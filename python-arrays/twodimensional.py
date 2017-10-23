#1.4.4. Случайные блуждания без самопересений
import random
import stdarray
import stdio

n =  22 #размер решетки
trials = 100000 #кол-во испытаний
deadEnds = 0 #
for t in range(trials):
    a = stdarray.create2D(n, n, False)
    x = n // 2 #
    y = n // 2
    while (x > 0) and (x < n-1) and (y > 0) and (y < n-1):
        deadEnds += 1
        break
    r = random.randrange(1, 5)
    if ( r == 1) and (not a[x+1][y]): x += 1
    elif (r == 2) and ( not a[x-1][y]): x -= 1
    elif (r == 3) and (not a[x-1][y]): y += 1
    elif (r == 4) and (not a[x][y-1]): y -= 1

stdio.writeln(str(100*deadEnds // trials) + '% dead ends')

#1.4.1 May be use random for this task

nums = [x for x in range(1000)]

print(nums[999])

#1.4.2 Создавть два вектора. Которые будут вычислять
# вычислять Евклидово Расстояние
# a = [1,2,3,4,5]
# b = [2,3,0,0,1]
# Как я понимаю нужно взять каждый элемент
# одного списка и второго, "перебрать"
# и сложить каждый элемент. Записать все в другой массив и вывести
# for i in a:
#     for j in b:
#         add

# То, типа как я решил. Нашел варианты через библиотеку и без
# def euclid_distance(first,second):
#     sumdist = 0.0
# # Суммируем квадраты
#     for i in range(len(first)):
#         sumdist += (first[i] - second[i]) ** 2
#         #Корень квадратный
#         return sumdist ** 0.5

# euclid_distance(4,2)

# Второй вариант. https://stackoverflow.com/questions/1401712/how-can-the-euclidean-distance-be-calculated-with-numpy
# from math import sqrt
# a = (1,2,3)
# b = (1,1,1)
# print(sqrt( sum(a - b)**2 for a, b in zip(a,b)))

# Третий вариант из книги.
import stdio

def eucld(p, q):
    if q == 0:
        return p
    return eucld(q, p % q)

def main():
    p = 2
    q = 2
    divisor = eucld(p, q)
    stdio.writeln(divisor)

if __name__ == '__main__':
    main()

#1.4.3
# Составить фрагмент кода меняющий на
# обратный порядок элементов в одном массиее
a = [2,3,3]
n = len(a)
for i in range(n // 2):
    temp = a[i]
    a[i] = a[n-1-i]
    a[n-1-i] = temp
print(temp)

# Второй способ
b = [1,2,3]
b[0], b[2] = b[2], b[0]
print(b)

# Третий способ
import random
x = [1,2,3,4]
random.shuffle(x)
print(x)

# Четверый способ
mylist = ['a','b','c']
myorder = [2,0,1]
mylist = [mylist[i] for i in myorder]
print(mylist)

#1.4.4
# Что не так со следующим фрагментом кода,
#
# a = []
# for i in range(10):
#     a[i] = i * i
# Массив пуст. Никаких элементов в последствии не добавится.
# Таким образом a[1], a[0] не существует.
# Во время выполнения кода, а конкретно выполнения оператора
# присваивания произойдет ошибка IndexError.

#1.4.5
#Составьте фрагмент кода, выводящий содержимое двумерного
# массива логических переменных, используя знак * для
# представления значения True и пробел для представления значения
# False .
# Выводите также номера рядов и столбцов.

# Задать массив с логическими значениями
# потом взять и перебрать в цикле каждый элемент массива. Потом
# Если тру то вывести * и значение " " для пробела. Как вывести номера столбцов
# и рядов?
a = [True,False, True, False, True, False]
for i in a:
    if i == True:
        print(" Will be *")
    if i == False:
        print(" will be space " "")



#1.4.6
# Что выводит следующий фрагмент кода
import stdarray
a = stdarray.create1D(10,0) # Создаем одномерный массив
for i in range(10): #для и в пределе 10
    a[i] = 9 - i  #запиши в итый элем. (т.е. в каждый 0,1,2 и тд) 9 - и.
    # Пример если идет на вход 0, то в место его мы запишем 9 - 0 = 9. И так с 9 до 0
for i in range(10):
    a[i] = a[a[i]]
    for v in a:
        stdio.writeln(v)

#1.4.7
# Что выведет код?
n = 25
a = [0, 1]
for i in range(2, n):
    a += [a[i-1] + a[i-2]]
print(a)
#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89 Числа Фибоначчи

#1.4.8.
# Составьте  программу, получающую аргумент командной строки n и выводящую
# n разделенных пустыми строками комбаниций карт ( по пять в каждой) из
# перетасованной колоды.




#1.4.9
#
#
def gen_matrix( m, n, k):
    result = []
    for _ in range(m):
        result.append([k] * n)
    return result

print(gen_matrix(2,4,0))