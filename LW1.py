# coding=utf-8
import numpy as np

import gauss

# https://github.com/aliot2010/-Python_Gauss
# https://pyprog.pro/io_functions/savetxt.html
# https://pyprog.pro/array_creation/loadtxt.html
# https://www.easycoding.org/2017/01/23/schityvaem-chislovye-dannye-iz-fajla-na-python.html
# Задачи:
#   1) Решение СЛАУ.
#   2) Найти определитель матрицы.
#   3) Поиск обратной матрицы.

fName = 'input.txt'

# Тип задачи.
taskType = 1

# Размер матрицы.
matrixSize = 0

# Чтение типа задачи и размера матрицы.
# with open(fName) as inFile:
#    taskType = int(inFile.readline())
#    matrixSize = int(inFile.readline())

# Чтение матрицы коэффициентов из файла
# matrixA = np.loadtxt(fName,
#                     skiprows=2,
#                     usecols=(range(matrixSize)))
# print('Матрица A: ')
# print(matrixA)

# Чтение матрицы коэффициентов из файла
# matrixB = np.loadtxt(fName,
#                     skiprows=2,
#                     usecols=matrixSize)
# print('Матрица B: ')
#print(matrixB)

# Готовое решение СЛАУ
# x = np.linalg.solve(matrixA, matrixB)
# print('Решение СЛАУ: ')
#print(x)

# Готовое решение определителя матрицы.
# detA = np.linalg.det(matrixA)
# print('Определитель матрицы: ')
# print(detA)

# Готовое решение обратной матрицы.
# invA = np.linalg.inv(matrixA)
# print('Обратная матрица: ')
#print(invA)

# Тестовая запись файла.
#np.savetxt('test_output.txt', matrixA, fmt='%0.2f')


matrixAB = np.loadtxt(fName,
                      skiprows=2, )

matrixAnother = np.array([[2., 1, 1, 2],
                          [1, -1, 0, -2],
                          [3, -1, 2, 2]])
print("_____________________________________________________")
print("_____________________________________________________")

b = gauss.gaussFunc(matrixAnother)
print("Ответ:")
print(b)

