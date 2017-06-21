import threading

matrixA = [[7, 8], [7, 8]]
matrixB = [[9, 8], [8, 7]]

def calculate_element(row, col):
    result = 0

    for i, item in enumerate(row):
        result += item * col[i]
    return result

def calculate_row(rowA, matrixB):
    cols = [[row[i] for row in matrixB] for i in range(len(matrixB[0]))]
    result = list(map(lambda x: calculate_element(rowA, x), cols))
    print(result)
    return result

for row in matrixA:
    threading.Thread(target=calculate_row, args=(row, matrixB)).start()
