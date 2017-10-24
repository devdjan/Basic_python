# Рекурсивная функция Фибоначчи
#
#
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return(fibonacci(n-1)+fibonacci(n-2))

print(fibonacci(4)) # вернет нам три, т.к. н != 0 и н != 1. То

# выполняем условие return(fibonacci(3)+fibonacci(2))
# fibonacci(3) = (fibonacci(2)+fibonacci(1))
# fibonacci(2) = (fibonacci(1)+fibonacci(0))

# В итоге фибоначчи от 1 = 1
# Фибоначчи от 2 = фиб(1) + фиб(0) = 1
# Далее Фибоначчи от 3 = фиб(2) + фиб(1). Так как фибоначчи(2) = 1, то
# Фибоначчи(3) будет равно 1 + 1 = 2
# Фибоначчи от 4 = 2 + 1

# Все работает верно!


