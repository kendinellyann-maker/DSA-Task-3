
matrix = [
    [0, 0, 5],
    [0, 0, 0],
    [7, 0, 0],
]

rows = len(matrix)
cols = len(matrix[0])

triplets = []                       
for i in range(rows):
    for j in range(cols):
        if matrix[i][j] != 0:
            triplets.append([i, j, matrix[i][j]])


sparse = [[rows, cols, len(triplets)]] + triplets

print("Row Col Val")
for r in sparse:
    print(r[0], "  ", r[1], "  ", r[2])