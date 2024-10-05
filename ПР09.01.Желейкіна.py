import math

def coordinates(num_points):
    X = []
    Y = []
    for i in range(num_points):
        x = float(input(f"Введіть координату X для точки {i + 1}: "))
        y = float(input(f"Введіть координату Y для точки {i + 1}: "))
        X.append(x)
        Y.append(y)
    return tuple(X), tuple(Y)

num_points = int(input("Введіть кількість точок: "))

X, Y = coordinates(num_points)

distances = []

for i in range(len(X)):
    for j in range(i + 1, len(X)):
        distance = math.sqrt((X[j] - X[i])**2 + (Y[j] - Y[i])**2)
        distances.append(distance)

print("Відстані між кожною парою точок:", distances)