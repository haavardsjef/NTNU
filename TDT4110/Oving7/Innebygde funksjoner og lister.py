# Innebygde funksjoner og lister, Oving 7 ITGK
# Håvard Hjelmeseth


# Importer moduler
import random


# Definer funksjoner
def antall_i_liste(list, number):
    n = 0
    for element in list:
        if element == number:
            n += 1
    return n


def sum_av_liste(list):
    sum = 0
    for element in list:
        sum += element
    return sum


def typetall(list):
    x = 0
    tall = 0
    for i in range(1, 11):
        if list.count(i) > x:
            x = list.count(i)
            tall = i
    return tall


# Lag lister
random_numbers = []
for i in range(100):
    random_numbers.append(random.randint(1, 10))


# Kall funksjoner
print("Number of 2s:", antall_i_liste(random_numbers, 2))
print("Sum of numbers:", sum_av_liste(random_numbers))
random_numbers.sort()
print("Numbers sorted:", random_numbers)
print("There are most of number:", typetall(random_numbers))
random_numbers.reverse()
print("Numbers reversed:", random_numbers)
