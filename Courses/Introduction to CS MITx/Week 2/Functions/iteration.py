def factorial_iteration(n):
    prod = 1
    for i in range(1, n):
        prod *= i
    return prod

print(factorial_iteration(3))