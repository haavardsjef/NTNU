#Generelt om betingelser av Håvard Hjelmeseth , Øving 2 ITGK

x = float(input("Skriv inn ditt første tall: "))	#Første tallvaribel, input av bruker
y = float(input("Skriv inn ditt andre tall: "))		#Andre tallvariabel

sum = x + y				#Summerer første og andre tallvariabel og lagrer i en variabel sum
prod = x * y			#Tar produktet av første og andre variabel og lagrer i en variabel prod

if sum < prod:										#Hvis summen av de to tallvariablene er mindre en produktet av dem	
	print("Summen av", x, "og", y, "er", sum,		#Printer at summen har lavere verdi enn produktet		
	"og er mindre enn produktet av de to.")

elif sum > prod:									#Hvis summen av de to tallvariablene er større enn produktet av dem
	print("Produktet av", x, "og", y, "er",			#Printer at produktet har lavere verdie enn summen
	prod, "og er mindre enn summen av de to")
	
else:												#Hvis ingen av de to betingelsene over er sann, dvs at summen må være lik produktet
	print("Summen og produktet av de to",			#Printer at summen er lik produktet
	"tallene er begge:", sum)