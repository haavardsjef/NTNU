# Osteviruset, Oving 9 ITGK
# Håvard Hjelmeseth


# Startbetingelser
cheeses = {
    'cheddar':
    ('A235-4', 'A236-1', 'A236-2', 'A236-3', 'A236-5', 'C31-1', 'C31-2'),
    'mozarella':
    ('Q456-9', 'Q456-8', 'A234-5', 'Q457-1', 'Q457-2'),
    'gombost':
    ('ZLAFS55-4', 'ZLAFS55-9', 'GOMBOS-7', 'A236-4'),
    'geitost':
    ('SPAZ-1', 'SPAZ-3', 'EMACS45-0'),
    'port salut':
    ('B15-1', 'B15-2', 'B15-3', 'B15-4', 'B16-1', 'B16-2', 'B16-4'),
    'camembert':
    ('A243-1', 'A234-2', 'A234-3', 'A234-4', 'A235-1', 'A235-2', 'A235-3'),
    'ridder':
    ('GOMBOS-4', 'B16-3'),
}
print('''Hylleplasser til osten "port salut”:''')
print(cheeses["port salut"])


# Infected cheeses
infected_cheeses = []
infected_shelves = ["B13-", "B14-", "B15-", "A234", "A235", "C31-"]

for ost in cheeses:
    for hylle in cheeses[ost]:
        if hylle[: 4] in infected_shelves:
            infected_cheeses.append(ost)

print()
# Bruker list(set()) for å kvitte meg med duplikater
print("Potentially infected cheeses:")
print(list(set(infected_cheeses)))

print()
print("Friske oster:")
for ost in cheeses:
    if ost not in infected_cheeses:
        for hylle in cheeses[ost]:
            print(hylle, ",", ost)
