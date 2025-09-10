# С помощью цикла создайте матрицу 10x10 и ещё одну - такой же размерности
# Теперь вам нужно сложить эти две матрицы в третью.
#
# Задание считается выполненным, если вы напишите алгоритм, который будет уметь как складывать матрицы,
# так и генерировать матрицы различных размерностей. Будь то матрицы 10х10 или 4х3.

from random import randint as rand

def generate_mx(x,y):
    return [[rand(-100,100) for x in range(x)] for y in range(y)]

def print_mx(mx):
    for row in mx:
        for elem in row:
            print("% 4d" % elem, end=" ")
        print("")

def sum_mx(mx_a, mx_b):
    if len(mx_a) != len(mx_b):
        raise ValueError("mx_a and mx_b must have same length")
    if len(mx_a) == 0:
        return []

    mx_result = []
    for i in range(len(mx_a)):
        mx_result.append([])
        for j in range(len(mx_a[0])):
            mx_result[i].append(mx_a[i][j] + mx_b[i][j])
    return mx_result


mx1 = generate_mx(5, 5)
mx2 = generate_mx(5, 5)
mx_sum = sum_mx(mx1, mx2)

print("Mx #1:")
print_mx(mx1)

print("Mx #1:")
print_mx(mx2)

print("Mx SUM:")
print_mx(mx_sum)
