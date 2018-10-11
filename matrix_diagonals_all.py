mat = [ [1, 3, 6, 10],
        [2, 5, 9, 13],
        [4, 8, 12, 15],
        [7, 11, 14, 16]
    ]

def matrix_diagonals(mat):
    rows = len(mat)
    cols = len(mat[1])

    for rowNo in range(rows):
        i = rowNo
        j = 0
        while(i >= 0):
            print(mat[i][j])
            j += 1
            i -= 1

    for colNo in range(1, cols):
        i = cols - 1
        j = colNo
        while(j <= cols-1):
            print(mat[i][j])
            j += 1
            i -= 1


matrix_diagonals(mat)
print("=================================")

mat_2 = [[ 7,  4,  2,  1],
         [11,  8,  5,  3],
         [14, 12,  9,  6],
         [16, 15, 13,  10]
        ]

def mat_diagonal_all_reverse(mat):

    rows = len(mat)
    cols = len(mat[0])

    for colNo in range(cols-1, -1, -1):
        i = 0
        j = colNo
        while(j < cols):
            print(mat[i][j])
            i += 1
            j += 1

    for rowNo in range(1, rows):
        i = rowNo
        j = 0
        while(i < rows):
            print(mat[i][j])
            i += 1
            j += 1

mat_diagonal_all_reverse(mat_2)

