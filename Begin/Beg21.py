import math

x1 = int(input("x1 = "))
x2 = int(input("x2 = "))
x3 = int(input("x3 = "))
y1 = int(input("y1 = "))
y2 = int(input("y2 = "))
y3 = int(input("y3 = "))

a = round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 1)
b = round(math.sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2), 1)
c = round(math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2), 1)
p = (a + b + c) / 2

print("S = ", round(math.sqrt(p * (p - a) * (p - b) * (p - c)), 2))


