def cyclicRotation(array, n):
    shifts = n % len(array)

    newArray = array[-shifts:] + array[:-shifts]

    return newArray


print(cyclicRotation([3, 8, 9, 7, 6], 10))
print(cyclicRotation([3, 8, 9, 7, 6], 1))
print(cyclicRotation([3, 8, 9, 7, 6], 2))
print(cyclicRotation([3, 8, 9, 7, 6], 3))
print(cyclicRotation([3, 8, 9, 7, 6], 4))
print(cyclicRotation([3, 8, 9, 7, 6], 5))
