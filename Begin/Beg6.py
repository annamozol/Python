cubeEdge1 = input("length: ")
cubeEdge2 = input("width: ")
cubeEdge3 = input("height: ")
a = int(cubeEdge1)
b = int(cubeEdge2)
c = int(cubeEdge3)
V = a * b * c
S = 2 * (a * b + a * c + b * c)
print("V = ", V)
print("S = ", S)
