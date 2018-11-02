navn = input("Hva er ditt navn? ")											#Får brukerens navn og lagrer i variabel
alder1= int(input("Hva er din alder? "))									#Får brukerens alder
alder2= int(input("Hvor gammel var du når du begynte å programmere? "))		#Får hvor alder til bruker når h*n startet å programmere

print("Du heter", navn, "og er", alder1, "år gammel.")						#Printer brukers navn og 

prog = alder1-alder2														#Regner ut hvor lenge bruker ha programmert ved divisjon

if (prog < 0):																#Hvis bruker har programert i mindre en null år...
	print ("Du kan umulig ha programmert i", prog, "år???")
	
elif (prog == 0):															#Hvis bruker har programmert i mellom 0-1 år
	print ("Du har nettopp startet å programmere.. Så spennende!")

else:																		#Hvis bruker har programmert i mer enn ett år
	print("Du har programmert i", prog, "år.")								#Printer hvor lenge bruker har programert
	