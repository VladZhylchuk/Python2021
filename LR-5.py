def task1():
    counter = 0
    stroke_len = int(input("Enter amount of items : "))
    stroke = [0] * stroke_len
    for i in range(stroke_len):
        stroke[i] = int(input(f"item{i+1} : "))

    for i in range(1, stroke_len, 2):
        if stroke[i] > 0:
            counter += 1
    print(f"Positive numbers on even position : {counter}")


def task2():
    N = 15
    array = [i for i in range(N)]
    M = 4
    K = 3
    P = 8

    if M + K < N and M + P < N:
        temp = array[K: M + K]
        array[K: M + K] = array[P: M + P]
        array[P: M + P] = temp
        print(array)
    else:
        print("Can`t replace")


def task3():
    rows_len, cols_len = (2, 2)

    matrix = [[0 for i in range(cols_len)] for j in range(rows_len)]

    for i in range(cols_len):
        for j in range(rows_len):
            matrix[i][j] = int(input("Enter matrix values : "))

    for row in matrix:
        print(row)
    max = sum(matrix[0]) / rows_len

    for row in matrix:
        temp = sum(row) / rows_len
        if max < temp:
            max = temp
    print(f"Maximum among all rows: {max}")


def task4():
    matrix_size = 3
    matrix = [[1 for i in range(matrix_size)] for j in range(matrix_size)]
    for row in matrix:
        print(row)

    for i in range(matrix_size):
        for j in range(matrix_size):
            matrix[i][j] = int(input(f"Enter matrix[{i}][{j}] : "))

    for row in matrix:
        print(row)
    sum = 0
    for i in range(matrix_size):
        for j in range(matrix_size):
            if i == j + 1 or i == j - 1:
                sum +=  matrix[i][j]
    print(sum)

def task5():
    array = []
    digits = []
    user_input = '0'
    print("Fill the array \nDone - stop word")
    while user_input != "Done":
        array.append(user_input)
        user_input = input("add new item : ")

    for item in array:
        if "1234566789".find(item) !=  -1:
            digits.append((int(item), array.index(item)))
    for item, index in digits:
        print(f"{item} {index}")
    print(f"Digits in array: {len(digits)}")




