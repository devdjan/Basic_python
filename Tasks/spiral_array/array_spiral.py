# Generating Spiral matrix in python

def spiral_func(n):
    # Переменной дх присваивается значение 1
    # Переменной ду присваивается значение 0
    # dx и dyб это приращения для переменных х и у
    dx, dy = 1,0
    # Переменным ч и у присваивается значение 0
    x,y = 0, 0
    # Создаем список списков
    # Эт оматрица рамера н * н
    # Пока все её элем. - пустые (None)
    arr = [[None] * n for _ in range(n)]
    # Выполяем перебор соответвенно
    # Для переменной и последовательно перебираем значения от 1 до (н **(в квадратке) + 1) => (n**+1)
    for i in range(1, n**2+1):
        # Элементу мартрицы с координами х и у присваивается значение і
        # Эта строчка будет присваивать последовательный натуральные числа
        # Только тем ячейкам, которые перебирают код чуть ниже
        arr[x][y] = i
        # Создаются временные переменные нх и ну
        # в которых вычисляются новые значения для х и у
        # для этого к старым значениям прибавляются приращения
        nx, ny = x+dx, y+dy
        # Если все нормально, и индекс не выскочил за пределы матрицы
        # и не наткнулся на уже занятую ячейку
        if 0 <= nx < n and 0 <= ny < n and not arr[nx][ny]:
            # то эти значения и оставляются
            x, y = nx, ny
        else:
            # а если индекс вышел за границу матрицы
            # или наткнулся на уже зайнятую ячейку
            # то разворачивакмся на 90 градусов
            # путем замены приращения по х и у друг на друга
            # а " - " минус нужен, чтобы он не ходил только вправо или вниз,
            # а чередовал с движениями вверх или влево
            # Так и получается спираль
            dx, dy = -dy, dx
            # и используем уже это измененное движение для новых значений х и у
            x, y = x+dx, y+dy

    # После того, как перебрали все элементы
    # Выодим все то, что получилось у нас
    for x in list(zip(*arr)):
        print(*x)

# Вызываем вышеописанну. функцию
# Вызываем ее с аргументом, который вводит пользователь с клавиатуры
spiral_func(int(input()))



# 1
# The next example
# From stackoverflow
# First step: Pop top row
# Second step: Transpose and flip upside-down(same as
# rotate 90 degrees counter-clockwise)
# Go to 1 step
# ----------------------------------------------------
# 1. Верхнюю строчку, потом
# 2. Транспонирум и переворачиваем матрицу вверх-вниз,
# тоже самое что и вращение на 90 градусов против часовой стрелки
# 3. Вернуться к шагу 1


# arr = [[1,2,3,4],
#        [12,13,14,5],
#        [11,16,15,6],
#        [10,9,8,7]]
#
# def transpose_and_yield_top(arr):
#     while arr:
#         yield arr[0]
#         arr = list(reversed(zip(*arr[1:])))
#
# print list(itertools.chain(*transpose_and_yield_top(arr)))


# 2
# Generating spiral matrix we can treated like a snake moving tovards
# boundary an turning on when hitting the boundary or itself


ar = [
    [0, 1, 2, 3, 4],
    [15, 16, 17, 18, 5],
    [14, 23, 24, 19, 6],
    [13, 22, 21, 20, 7],
    [12, 11, 10, 9, 8]]

def print_spiral(ar):
    # if rect array
    rows, cols = len(ar), len(ar[0])
    r, c = 0, -1 # start here
    nextturn = stepsx = cols #move so many steps
    stepsy = rows - 1
    inc_c, inc_r = 1, 0# at each step move this much
    turns = 0 # how many times our snake had turned

    for i in range(rows, cols):
        c += inc_c
        r += inc_r

        print(ar[r][c]), # maybe row and cols

        if i == nextturn - 1:
            turns += 1
            # at each turn reduce how many steps we go next
            if turns % 2 == 0:
                nextturn += stepsx
                stepsy -= 1
            else:
                nextturn += stepsy
                stepsx -= 1
            # changing the Directions
            inc_c, inc_r = -inc_r, inc_c

print_spiral(ar)


# 3
# The same example
# Recursive

ar = [
    [0, 1, 2, 3, 4],
    [15, 16, 17, 18, 5],
    [14, 23, 24, 19, 6],
    [13, 22, 21, 20, 7],
    [12, 11, 10, 9, 8]]

def print_spiral(ar, sr=0, sc=0, er=None, ec=None):
    er = er or len(ar)- 1
    ec = ec or len(ar[0]) - 1

    if sr > er or sc > ec:
        print()
        return


    # print the outer layer
    top, bottom, left, right = [], [], [], []
    for c in range(sc, ec+1):
        top.append(ar[sr][c])
        if sr != er:
            bottom.append(ar[er][ec-(c-sc)])

    for r in range(sr+1, er):
        right.append(ar[r][ec])
        if ec != sc:
            left.append(ar[er-(r-sr)][sc])

    print(" ".join([str(a) for a in top + right + bottom + left])),
    # peel next layer of onion

    print_spiral(ar, sr + 1, sc + 1, er - 1, ec - 1)

