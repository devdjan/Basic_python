#spreadsheets of numbers
m = 5
n = 4
a = []
for i in range(m):
    # Среднее для ряда i
    total = 0.0
    for j in range(n):
        total += a[i][j]
    a[i][n] = total / m