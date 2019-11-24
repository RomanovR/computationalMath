import numpy as np


def main():
    task_type, matrix_size, matrix = read_matrix('input.txt')

    # Задачи:
    #   1) Решение СЛАУ.
    #   2) Найти определитель матрицы.
    #   3) Поиск обратной матрицы.
    if task_type == 1:
        print("Решить СЛАУ")
        solve(matrix, matrix_size)
    elif task_type == 2:
        print("Найти определитель матрицы")
        print("Определитель матрицы равен: ")
        print(det(matrix, matrix_size))
    elif task_type == 3:
        print("Поиск обратной матрицы")



def read_matrix(file_name):
    # Чтение типа задачи и размера матрицы.
    with open(file_name) as inFile:
        task_type = int(inFile.readline())
        matrix_size = int(inFile.readline())

        # Чтение матрицы коэффициентов из файла
        matrix_a = np.loadtxt(file_name,
                              skiprows=2)
        print('Матрица A: ')
        print(matrix_a)
    return task_type, matrix_size, matrix_a


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
    # row_max = int(np.argmax(matrix[:, 0]))
    #
    # if row_max != 0:
    #     matrix[[0, row_max], :] = matrix[[row_max, 0], :]

    print("Отсюда дебаг___________________")

    for rc in range(matrix_size):
        # Перемещаем строку с максимальным ведущим элементом в начало.

        row_max = int(np.argmax(matrix[rc:, 0]))
        if row_max != 0:
            # Обмен строками
            matrix[[rc, row_max], :] = matrix[[row_max, rc], :]

        # Делим первую строку на её первый элемент
        # matrix[rc, :] /= matrix[rc, rc]

        # Вычитаем из всех строк, кроме первой
        # matrix[rc+1:, rc:] += matrix[rc, :]

        # ПРОХОД СТУПЕНЬКАМИ
        # print(matrix[rc:, rc:])
        print("ITER ++")


    # for col in range(matrix_size):
    #     for row in range(matrix_size):
    #             print(matrix[col::][col:])
    #
    #     print("_________________COL ++")



    print("Матрица после деления: ")
    print(matrix)
            #print(matrix[row][row:])
            #print(matrix)

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


if __name__ == "__main__":
  main()