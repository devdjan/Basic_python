# Функция факториала, по итерациям (итеративная)
def factorial(number):
    product = 1
    for i in range(number):
        product = product * (i + 1)
    return product

print(factorial(4)) # 1 * 2 * 3 * 4 = 24