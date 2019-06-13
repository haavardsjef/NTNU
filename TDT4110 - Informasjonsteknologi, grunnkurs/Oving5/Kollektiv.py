#Kollektiv Oving 5 Håvard Hjelmeseth
def pris(age,bike):		#Funksjon som returner pris på enkelt billet som funksjon
	p = 0				#av alder og om du har sykkel
	if bike == "j":
		p += 50
	if age < 5:
		p += 0
	elif age < 21:
		p += 20
	elif age < 26:
		p += 50
	elif age < 61:
		p += 80
	return p
	
m = "j"
a = 0
while m == "j":			#Loop som kjører så lenge brukeren ønsker å kjøpe flere biletter.
	print("-----")
	print()
	x = int(input("Hva er din alder? "))
	y = input("Har du med deg sykkel(j/n)? ")
	a += pris(x,y)
	m = input("Ønsker du å kjøpe flere billetter(j/n)? ")
	if m == "j":
		print("Pris hittil:", a)
	print()
print("Du må betale kr", a)
input()