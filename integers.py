# 1
#n школьников делят k яблок поровну, неделящийся остаток остается в корзинке. Сколько яблок достанется каждому школьнику? Сколько яблок останется в корзинке?
#Программа получает на вход числа n и k и должна вывести искомое количество яблок (два числа).
n = int(input()) #14
k = int(input()) #4
# Выводите результат через print()
a = k // n
b = k - (a * n)
print(a)
print(b)
#Походу, чтобы отрефакторить можно использовать "Return"
# return(k // n)
# return(k - (a * n))
# or, good idea write it using print
n = 10
k = 24
print(n // k)
print(n % k)

# 2
# Дано число n. C начала суток прошло n минут. Определить, сколько часов и минут будут показывать электронные часы
# в тот момент. Вывести два числа. Кол-во часов (0 - 23) и минут (0 - 59)/Учтите, что число n может быть больше, чем количество минут в сутках.
# 24 - 1440
n = 1233
hours = n // 60
minutes = n % 60
print(hours,minutes)
# Возвращаем остаток от деления(частное числ) n/60 - будет 20 часов
# 1233 // 60 = 20 |
# Модульб числа. Например 10 % 9 = 1. Остаток - еденица.
# 1233 % 60 = 33 остаток. В итоге время 20 часов 33 минуты.

hour = n // 60 % 24


#-----------------------------------------------------
# Tasks from task.txt
#-----------------------------------------------------

# At that part examples from tasks.txt
#Define triangle. And decide exist it or not?
def triangle (a,b,c):
    if (a < b + c) and (b < c + a) and (c < a + b):
        print("True")
    else:
        print("False")
triangle(4,5,6)
#or change return for "Print (Triangle exist) etc."



# Better way of solving this task. Algorithmi is the same:
# Define function triangle which take
# three parameters a,b,c. Then we does'nt print out true, false,
# we use "Return"(true of false)

# def triangle (a,b,c):
#     return (a < b + c) and (b < c + a) and (c < a + b)
#         return false

# Testing values
# We are checking how our program works( correctly or not),
# with different values

# list_check : {
#     0,0,0 : False,
#     1,2,3 : True
# }
#Loop for using
# any(*variable). ()python tuples

#--------------------------------------------------------
# FizzBuzz
#--------------------------------------------------------
for i in range(1,100):
    if i % 3 == 0:
        print("Fizz")
    if i % 5 == 0:
        print("Buzz")
    if i % 15 == 0:
        print("FizzBuzz")
    else:
        print(i)