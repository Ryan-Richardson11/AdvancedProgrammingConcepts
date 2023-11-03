import math


def quadraticEquation(a, b, c):
    a, b, c = int(a), int(b), int(c)
    
    if ((b**2) - (4 * a * c)) < 0:
        return None
    else:
        x1 = (-b + math.sqrt((b**2) - (4 * a * c))) / (2 * a)
        x2 = (-b - math.sqrt((b**2) - (4 * a * c))) / (2 * a)
        return (str(x1), str(x2))


# python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. QuadraticEquation.proto
