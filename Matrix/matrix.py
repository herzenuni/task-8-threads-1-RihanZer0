import threading

A = [[7, 8], [7, 8]]
B = [[9, 8], [8, 7]]

def calculate_element(row, col):
    result = 0

    for i, item in enumerate(row):
        result += item * col[i]
    return result

def calculate_row(rowA, B):
    cols = [[row[i] for row in B] for i in range(len(B[0]))]
    result = list(map(lambda x: calculate_element(rowA, x), cols))
    print(result)
    return result

for row in A:
    threading.Thread(target=calculate_row, args=(row, B)).start()