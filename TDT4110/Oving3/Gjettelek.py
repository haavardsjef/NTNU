#Gjettelek av Håvard Hjelmeseth ITGK Øving 3
import random

upper_lim = int(input("Øvre grense: "))		#Øvre grense av ran_num
ran_num = random.randint(1,upper_lim)		#Tilfeldig tall mellom 1 og øvre grense

guess = int(input("Gjett et tall: "))		#Brukerens gjetning, input

while guess != ran_num:		#Løkke som kjører så lenge brukeren ikke har gjettet riktig
	if guess < ran_num:		#Gir hint om at brukeren må gjette høyere
		print("Gjett høyere!")
		guess = int(input("Gjett på nytt: "))
	else:					#Gir hint om at brukeren må gjette lavere
		print("Gjett lavere!")
		guess = int(input("Gjett på nytt: "))
print("Gratulerer, du gjettet riktig!")		#Gjettet riktig = løkke brutt
input()