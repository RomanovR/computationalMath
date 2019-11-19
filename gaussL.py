import numpy as np


# На вход подаем расширенную квадратную матрицу np
def solve(in_matrix, matrix_size):
    eps = 1e-16
    matrix = np.array(in_matrix)
    size = matrix_size

    if det(matrix, matrix_size) == 0.0:
        print("Определитель матрицы равен нулю.")
    else:
        for row in range(matrix_size):
            if in_matrix[row, :].any() == 0:
                print("Обнаружена нулевая строка.")
        for col in range(len(in_matrix[0])):
            if in_matrix[:, col].any() == 0:
                print("Обнаружен нулевой столбец.")


    print("Матрица сейчас:")
    print(matrix)

    # Перемещаем строку с максимальным ведущим элементом в начало.
    row_max = int(np.argmax(matrix[:, 0]))
    if row_max != 0:
        matrix[[0, row_max], :] = matrix[[row_max, 0], :]

    print("Матрица после перемещения строки с макс ведущим элементов на первое место:")
    print(matrix)

   # for row in range(matrix_size):
   #     try:
   #         print(matrix[row][:])
   #     except ZeroDivisionError:
   #         print()
    # бесполезная проверка на нулевые строки и столбцы
    # print("проход по строкам")
    # for row in range(matrix_size):
    #     print(in_matrix[row, :].any())
    # print("проход по столбцам")
    # for col in range(len(in_matrix[0])):
    #     print(in_matrix[:, col].any())

    # Нормирование матрицы


def det(in_matrix, matrix_size):
    detM = in_matrix[0][0]
    for rc in range(matrix_size):
        detM = detM * float(in_matrix[rc][rc])
    return detM

