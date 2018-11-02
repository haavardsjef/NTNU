#Spiralfirkant - Håvard Hjelmeseth ITGK Øving 3

side = 250				#Første side er 250 pixler
from turtle import *	#Importer turtle

 
while side > 0:			#Hindrer sidelengden fra å bli negative verdier
   forward(side)
   left(90)
   side -= 7