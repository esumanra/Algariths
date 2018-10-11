mat = [[1, 2, 3, 4, 5],
       [14, 15, 16, 17, 6],
       [13, 20, 19, 18, 7],
       [12, 11, 10, 9, 8],
       ]


def spiral_matrix(mat, m, n):
    r = 0
    c = 0
    last_row = len(mat) - 1
    last_col = len(mat[1]) - 1

    while r <= last_row and c <= last_col:
        for i in range(c, last_col + 1):
            print(mat[r][i])
        r += 1

        for i in range(r, last_row + 1):
            print(mat[i][last_col])
        last_col -= 1

        for i in range(last_col, c - 1, -1):
            print(mat[last_row][i])
        last_row -= 1

        for i in range(last_row, r - 1, -1):
            print(mat[i][c])
        c += 1


spiral_matrix(mat, len(mat), len(mat[0]))
