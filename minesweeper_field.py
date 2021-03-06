"""

Поле для игры сапёр представляет собой сетку размером n×m. В ячейке сетки может находиться или отсутствовать мина. 

Напишите программу, которая выводит "решённое" поле, т.е. для каждой ячейки, не являющейся миной, указывается число мин, находящихся в соседних ячейках (учитывая диагональные направления)

Формат ввода:
На первой строке указываются два натуральных числа 1≤n,m≤100, после чего в n строках содержится описание поля в виде последовательности точек '.' и звёздочек '*', где точка означает пустую ячейку, а звёздочка − ячейку с миной.

Формат вывода:
n строк поля, в каждой ячейке которого будет либо число от 0 до 8, либо мина (обозначенная символом "*"), при этом число означает количество мин в соседних ячейках поля.

Sample Input:

4 4
..*.
**..
..*.
....
Sample Output:

23*1
**32
23*1
0111
"""

import sys


def solve_field(n, m, field):
    for i in range(n):
        for j in range(m):
            if field[i][j] == 0:
                for di in range(-1, 2):
                    for dj in range(-1, 2):
                        ai = i + di
                        aj = j + dj
                        if 0 <= ai < n and 0 <= aj < m and field[ai][aj] == '*':
                            field[i][j] += 1
    return field


def main():
    reader = (line.rstrip('\n') for line in sys.stdin)
    n, m = map(int, next(reader).split())
    field = [[p if p == '*' else 0 for p in line] for line in reader]
    for line in solve_field(n, m, field):
        print(*line, sep='')


if __name__ == '__main__':
    main()
