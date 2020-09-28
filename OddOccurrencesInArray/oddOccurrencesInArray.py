def oddOccurrencesInArray(array):
    odd = 0
    for a in array:
        odd = odd ^ a
    return odd


def oddOccurrencesInArrayS(array):
    odd = set()
    for a in array:
        if a in odd:
            odd.remove(a)
        else:
            odd.add(a)

    return odd.pop()


print(oddOccurrencesInArray([1, 2, 3, 3, 5, 2, 1]))
print(oddOccurrencesInArrayS([1, 2, 3, 3, 5, 2, 1]))
