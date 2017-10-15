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
