# Gangetabell og Lister, Oving 7 ITGK
# Håvard Hjelmeseth


# definer funksjoner
def separate(numbers, threshold):
    upper = []
    lower = []
    for element in numbers:
        if element < threshold:
            lower.append(element)
        else:
            upper.append(element)
    return lower, upper


def multiplication_table(n):
    list = []
    row = []
    for i in range(1, n + 1):
        for x in range(1, n + 1):
            row.append(i * x)
        list.append(row)
        row = []
    return list


# kall funksjonene
list = [1, 7, 3, 8, 5, 9]
print(separate(list, 5))
print(multiplication_table(4))
