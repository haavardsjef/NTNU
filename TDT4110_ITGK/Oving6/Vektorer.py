# Importer moduler
import math

# Definer funksjonene


def vektor(x, y, z):  # Lager en liste av x,y,z koordinater
    return [x, y, z]


def vecprint(vec):  # Printer vektoren på en fin måte
    print("vector =", vec)


# Returnerer en vektor som er den forrige vektoren ganget med en skalar
def scalar_multiplication(vec, scalar):
    product = []
    for i in range(0, len(vec)):
        product.append(vec[i] * scalar)
    return product


def length(vec, scalar):  # Printer lengden av en vektor, lengden av vektoren etter skalarmulitplikasjonen og forholdet mellom de to
    v2 = scalar_multiplication(vec, scalar)
    l1sqrd = 0
    l2sqrd = 0
    for i in range(0, len(vec)):
        l1sqrd += vec[i]**2
        l2sqrd += v2[i]**2
    print("Vektorlengde:", math.sqrt(l1sqrd))
    print("Vektorlengde etter skalarmultiplikasjon:", math.sqrt(l2sqrd))
    print("Forholdet mellom de to er:", math.sqrt(l2sqrd) / math.sqrt(l1sqrd))
    return


def scalar_product(vec1, vec2):  # Returnerer skalarproduktet av to vektorer
    product = 0
    for i in range(0, len(vec1)):
        product += vec1[i] * vec2[i]
    return product


# Definer initialbetingelser
scalar = float(input("Oppgi en valgfri skalar: "))
vec1 = vektor(1.5, 3.7, 4.5)
vec2 = scalar_multiplication(vec1, scalar)
vec3 = vektor(3.7, -1.5, 0)


# Kaller funksjonene
vecprint(vec2)
print()
length(vec1, scalar)
print()
print(scalar_product(vec1, vec3))
