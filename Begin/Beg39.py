import math

factor1 = input("Enter A: ")
A = int(factor1)
factor2 = input("Enter B: ")
B = int(factor2)
factor3 = input("Enter C: ")
C = int(factor3)

D = B ** 2 - 4 * A * C
x1 = (- B + math.sqrt(D)) / (2 * A)
x2 = (- B - math.sqrt(D)) / (2 * A)
print("x1 = ", x1)
print("x2 = ", x2)

