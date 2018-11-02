#Regulært Polygon - Håvard Hjelmeseth ITGK - Øving 3
from turtle import *

print("Jeg kan tegne et regulært polygon.")

NumEdg = int(input("Velg antall kanter: "))		#Antall kanter i polygnet
O = int(input("Velg omkrets på polygonet: "))	#Omkrets på polygonet

for i in range(NumEdg):
	forward(O / NumEdg)		#Omkrets delt på antall sider
	left (360 / NumEdg)		#360 grader delt på antall vinkler