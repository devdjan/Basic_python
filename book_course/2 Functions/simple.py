def f(n):
    return n * 10 + 5

#Введите её в интерпретаторе и посчитайте,
# чему равно значение следующего выражения:
# f(10) = 105
# f(f(10))= f(105) = 1055
# f(f(f(10))) = 10555
print(f(f(f(10))))

# Minimum Function
def min(*a): # Принимает произвольное кол-во аргументов
    m = a[0]
    for x in a:
        if m > x:
            m = x
        return m

# Some king of Default function "Range"
def my_range(start, stop, step=1):
    result = []
    if step > 0:
        x = start
        while x < stop:
            result += [x]
            x += step
    elif step < 0:
        x = start
        while x > stop:
            result += [x]
            x += step
        return result

# Transfering parametres by it's names
# function print( end="") - which will return each number on new string
# What i mean, when we call fucntion
my_range(stop=20,start=5) # One variant
# короче, мы хоть и переставили значения, но так как вызываем обращаять по имени, у нас не будет ошибки
print(my_range(2,5,1))