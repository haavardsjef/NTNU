# Lett og blandet om lister Øving 6


def is_six_at_edge(list1):
    if list1[0] == 6 or list1[-1] == 6:
        return True
    else:
        return False


def average(list):
    return sum(list) / len(list)


def median(list):
    list.sort()
    return list[len(list) // 2]


liste1 = [1, 100, 8, 4, 3.5, 6, 20]
liste2 = [6, 8, 9, 10]

print(is_six_at_edge(liste1))
print(is_six_at_edge(liste2))

print(average(liste1))
print(median(liste1))
