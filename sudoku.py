import math

n = int(input('enter the size'))
s = []
pos_list = []

for i in range(0, n):
    s.append([])
    for j in range(0, n):
        s[i].append(j)
        s[i][j] = input()

for i in range(0, n):
    for j in range(0, n):
        s[i][j] = int(s[i][j])

for i in range(0, n):
    for j in range(0, n):
        if s[i][j] == 0:
            pos_list.append(tuple((i, j)))


def check(row, col, num, n):
    temp = int(row) % n
    v = int(col) % n

    for i in range(row - temp, (row - temp) + n):
        for j in range(col - v, (col - v) + n):
            if s[i][j] == num:
                return False

    # for i in range(row, n):
    #  for j in range(col - v, (col - v) + n):
    #     if s[i][j] == num:
    #        return False

    return True


def is_possible(row, col, num, n):
    for r in range(0, n):
        if num == s[row][r]:
            return False

    for p in range(0, n):
        if num == s[p][col]:
            return False

    return check(row, col, num, int(math.sqrt(n)))


def sudoku(pos, num, n):
    while num <= n:
        row = pos_list[pos][0]
        col = pos_list[pos][1]
        start = is_possible(row, col, num, n)
        if start is False:
            num = num + 1
        else:
            s[row][col] = num
            if pos == len(pos_list) - 1:
                return True
            else:
                res = sudoku(pos+1, 1, n)
                if res is True:
                    return True
                else:
                    s[row][col] = 0
                    num += 1

    return False


sudoku(0, 1, n)


def printl():
    print(s)


printl()
