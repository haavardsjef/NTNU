# Generelt om dictionary, Oving 9 ITGK
# Håvard Hjelmeseth


# Definer funksjoner
def add_family_member(role, name):
    if role in my_family.keys():
        my_family[role].append(name)
    else:
        my_family[role] = [name]
    return


# Startbetingelser
my_family = {}


# Test av kode
add_family_member('bror', 'Arne')
add_family_member('mor', 'Anne')
add_family_member('bror', 'Geir')
print(my_family)
