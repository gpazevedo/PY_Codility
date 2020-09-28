def binaryGap(number):
    longest = 0
    size = 0
    one = False

    while number > 0:
        if number & 1 > 0:
            if size > 0:
                longest = size if size > longest else longest
                size = 0
            else:
                one = True
        elif one:
            size += 1

        number = number >> 1

    return longest


print(binaryGap(1041))
print(binaryGap(32))
print(binaryGap(0))
print(binaryGap(1))
print(binaryGap(2))
print(binaryGap(32))
print(binaryGap(127))
print(binaryGap(1029))
