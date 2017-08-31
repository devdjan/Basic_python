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

#6 task
# import math
# import sys
# import stdio
#
# b = float(sys.argv[1])
# c = float(sys.argv[2])
#
# discriminant = b*b - 4.0*c
# d = math.sqrt(discriminant)
# stdio.writeln((-b + d) / 2.0)
# stdio.writeln((-b - d) / 2.0)





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
n = 4
a = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if i < j:
            a[i][j] = 0
        elif i > j:
            a[i][j] = 2
        else:
            a[i][j] = 1
for row in a:
    print(' '.join([str(elem) for elem in row]))



