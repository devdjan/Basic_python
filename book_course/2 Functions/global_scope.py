def print_value():
    print(a)

a = 5
print_value() # 5

# def print_value1():
#     print(a)
#     a = 10 # так как мы изменяем переменную внутри функции, считаем ее локальной
#     print(a)
#
# a = 5
# print_value1()


def f(x):
    # put your python code here
    if x <= -2:
        return 1 - (x + 2) ** 2
    if x <= 2 or x > -2:
        return -(x / 2)
    elif 2 < x:
        return (x - 2) ** 2 + 1


print(f(2))