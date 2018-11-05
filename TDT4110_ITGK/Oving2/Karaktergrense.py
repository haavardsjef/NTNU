#Karaktergrense av Håvard Hjelmeseth - Øving 2 ITGK

def kalk(pts):					#En funksjon som regner ut karakter basert på antall poeng
	if pts < 41:				#Hvis antall poeng er lavere enn 41 lagre karakteren F
		karakter = "F"
	elif pts < 53:				#Hvis antall poeng ligger mellom 40 og 53 lagre karakteren E
		karakter = "E"
	elif pts < 65:				#Hvis antall poeng ligger mellom 52 og 65 lagre karakteren D
		karakter = "D"
	elif pts < 77:				#Hvis antall poeng ligger mellom 64 og 77 lagre karakteren C
		karakter = "C"
	elif pts < 89:				#Hvis antall poeng ligger mellom 76 og 89 lagre karakteren B
		karakter = "B"
	else:						#Hvis antall poeng ligger over 88 lagre karakteren A
		karakter = "A"
	return karakter;			#Returner karakteren

def main():			#Hovedfunksjon, brukt til å restarte programmet om det oppstår en feil

	poeng = float(input("Skriv inn din poengsum: "))			#Lagre brukerens poengscore i en variabel
	
	if poeng != int(poeng):										#Sjekker om brukerens poengscore er et heltall
		print("Det er ikke ett heltall! Prøv på nytt...")		#Kjefter på brukeren dersom poengscoren ikke er et heltall,
		print()													#og restarter programmet
		print()
		main()
	elif poeng < 0:												#Hvis antall poeng er et negativt tall, kjefte på
		print("Velg ett tall mellom 0 og 100! Prøv igjen...")	#brukeren og restarte programmet
		print()
		print()
		main()
	elif poeng > 100:											#Hvis antall poeng er høyere enn 100, kjefte på
		print ("Velg et tall mellom 0 og 100! Prøv igjen...")	#brukeren og restarte programmet
		print()
		print()
		main()
	else:														#Hvis ingen av de over stemmer, så må det være et heltall mellom
		print("Din karakter er:", kalk(poeng))					#0 og 100 og dermed kjører vi kalk funksjonen og oppgir svaret.
	return
	
main()	#Setter i gang programmet etter at de to funksjonene er definert.