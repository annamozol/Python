import math

s = int(input("S = "))    #S = 3.14 * r ** 2
r = round(math.sqrt(s / 3.14), 2)

print("D = ", round(2 * r, 2))
print("L = ", round(2 * 3.14 * r, 2))
