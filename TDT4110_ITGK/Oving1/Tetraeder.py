#Tetraeder/Øving 1 av Håvard Hjelmeseth

h = float(input("Skriv inn en høyde: "))									#Får høyde fra bruker og lagrer i variabel
a = (3*h)/(6**(1/2))														#Angir verdien for a, spesielt for denne oppgaven.

area = round((3**(1/2))*(a**2), 2)											#Lagrer verdien av arealet i en variabel og runder av til to desimaler
volume = round(((2**(1/2))*(a**3)/(12)), 2)									#Lagrer verdien av volumet i en variable og runder av til to desimaler

print("En tetraeder med høyde", h, "har volum", volume, "og areal", area)	#Printer sammensatt setning av strings og de utregnede verdiene