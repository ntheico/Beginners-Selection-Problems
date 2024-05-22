def Triangle(X,Y,Z):
    if X > Y and X > Z:
        maximum = X
        side1 = Y
        side2 = Z
    if Y > X and Y > Z:
        maxiumum = Y
        side1 = X
        side2 = Z
    if Z > X and Z > Y:
        maximum = Z
        side1 = Y
        side2 = X

    sumSides = side1+side2
    if sumSides > maximum:
        return True
    else:
        return False

answer = Triangle(1,1,5)
print(answer)
