import math


def quadraticEquation():
    a = int(input("What is the value of a: "))
    b = int(input("What is the value of b: "))
    c = int(input("What is the value of c: "))

    if ((b**2) - (4 * a * c)) > 0:
        return "The answer does not exist"
    else:
        x1 = (-b + math.sqrt((b**2) - (4 * a * c))) / (2 * a)
        x2 = (-b - math.sqrt((b**2) - (4 * a * c))) / (2 * a)
        return (str(x1), str(x2))
