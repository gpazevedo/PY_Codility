def permMissingElem(integers):
    all = set(integers)

    for i in range(1, len(integers)+1):
        if not i in all:
            return i

    return len(integers)+1


print(permMissingElem([2]))
print(permMissingElem([1, 2]))
print(permMissingElem([3, 2]))
print(permMissingElem([2, 3, 1, 5]))
print(permMissingElem([3, 4, 1]))
