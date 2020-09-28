import math


def frogJmp(X, Y, D):
    return math.floor((Y - X) / D)


print(frogJmp(10, 85, 30))
