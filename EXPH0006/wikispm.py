# Wikispm, skrevet av Håvard Hjelmeseth
# 01.11.2018

# Programmet velger et tilfeldig spørsmål fra wikioppgavene

# Importer moduler
import random
# Hovedfunksjon

n = int(input("Hvor mange spørsmål vil du ha? "))

filnavn = "wikispm.txt"
f = open(filnavn, 'r', encoding='utf-8')
spm = f.readlines()
f.close()

for i in range(n):
    print()
    rand = random.randint(0,len(spm)-1)
    print(spm[rand])
    spm.pop(rand)
    print()
    input()
