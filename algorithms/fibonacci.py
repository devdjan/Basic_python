# Рекурсивная функция Фибоначчи
# Упростил функцию. Разобрался как работает.
#
def fibonacci(n):
    print("Fibonacci: "+str(n)) # Чтобы посмотреть как программа вызывается и какие значения берет
    if n < 2:
        return n
    else:
        return(fibonacci(n-1)+fibonacci(n-2))

print(fibonacci(4)) # вернет нам три, т.к. н != 0 и н != 1. То
# выполняем условие return(fibonacci(3)+fibonacci(2))
# fibonacci(3) = (fibonacci(2)+fibonacci(1))
# fibonacci(2) = (fibonacci(1)+fibonacci(0))

print(fibonacci(3)) #


