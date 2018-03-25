def gcdRecur(x, y):
    if y == 0:
        return x
    else:
        return gcdRecur(y, x % y)

print(gcdRecur(9, 3))