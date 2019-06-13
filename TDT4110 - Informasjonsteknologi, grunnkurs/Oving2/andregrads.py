# Andregradslikning av Håvard Hjelmeseth - ITGK Øving 2

a = float(input("Hva er A: "))		#Lagrer variabel a
b = float(input("Hva er B: "))		#Lagrer variabel b
c = float(input("Hva er C: "))		#Lagrer variabel c

d = ((b**2)-4*a*c)		#Regner ut d som er inni rotuttrykket

if d < 0:		#Hvis d er mindre enn 0 si at det er to imaginære løsninger
	print("Andregradslikningen har to imaginære løsninger")
elif d > 0:		#Hvis d er større enn 0 si at det er to reelle løsninger
	print("Andregradslikningen har to reelle løsninger")
else:			#Hvis ikke, dvs. d = 0 si at det er en dobbeltrot
	print("Andregradslikningen har én reell dobbeltrot")