#n школьников делят k яблок поровну, неделящийся остаток остается в корзинке. Сколько яблок достанется каждому школьнику? Сколько яблок останется в корзинке?
#Программа получает на вход числа n и k и должна вывести искомое количество яблок (два числа).
n = int(input()) #14
k = int(input()) #4
# Выводите результат через print()
a = k // n
b = k - (a * n)
print(a)
print(b)


#Maybe good idea write it using print
print(n // k)
print(n % k)



#-----------------------------------------------------
# Tasks from task.txt
#-----------------------------------------------------

# At that part examples from tasks.txt
#Define triangle. And decide exist it or not?
a = 3
b = 7
c = 9
def triangle (a,b,c):
    if (a < b + c) and (b < c + a) and (c < a + b):
        print("True")
    else:
        print("False")
#or change return for "Print (Triangle exist) etc."

#Write an function wich creates and initialises matrix. Entry  - m,n,k
#m, n height and width. K - element wich will be initialising the matrix.

#Testing,  i want to know how built matrix, before start




