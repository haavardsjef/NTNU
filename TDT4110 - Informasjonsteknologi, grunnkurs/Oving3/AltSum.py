#Alternerends sum - Håvard Hjelmeseth
n = int(input("n = "))		#Antall ledd i summen
k = int(input("k = "))		#Øvre grense av summ
Sum = 0						#Definerer variabelen sum med startverdi 0
x = 1						#Brukes for å holde øye med hvor mange ledd som er i summen

while Sum <= k and x < n+1:
	if x % 2 == 0:		#Sjekker om x er partall
		Sum -= x**2
	else:				#Om x er oddetall
		Sum += x**2
	x += 1
if Sum >= k:			#"trekker ifra" igjen det forrige leddet dersom summen overstiger k
	if x-1 % 2 == 0:
		Sum += (x-1)**2
	else:
		Sum -= (x-1)**2
	print("Den minste summen av tallserien under", k,"er", Sum,"Tallserien har", x-2, "elementer")
else:
	print("Summen av tallserien er:", Sum)
input()
