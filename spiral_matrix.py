"""
7  8  9
6  1  2
5  4  3
"""
import numpy as np


def generate_circle(num, left, top, right, down, matrix):
    if left == right and top == down:
        matrix[top][left] = num
        num += 1
        return num

    cur_i = top + 1
    cur_j = right
    while cur_i < down:
        matrix[cur_i][cur_j] = num
        cur_i += 1
        num += 1
    while cur_j > left:
        matrix[cur_i][cur_j] = num
        cur_j -= 1
        num += 1
    while cur_i > top:
        matrix[cur_i][cur_j] = num
        cur_i -= 1
        num += 1
    while cur_j <= right:
        matrix[cur_i][cur_j] = num
        cur_j += 1
        num += 1
    return num


def generate_spiral_matrix(n):
    matrix = np.zeros((n, n), dtype=np.int32)
    num = 1
    top = left = down = right = n//2
    while top >= 0 and left >= 0 and down <= n and right <= n:
        num = generate_circle(num, left, top, right, down, matrix)
        left -= 1
        top -= 1
        right += 1
        down += 1
    return matrix


if __name__ == '__main__':
    n = 9
    matrix = generate_spiral_matrix(n)
    for i in range(n):
        for j in range(n):
            print('{0:<6}'.format(matrix[i][j]), end=' ')
        print()
