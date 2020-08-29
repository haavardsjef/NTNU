#Eksempel på hvordan lese fra fil til en liste
f = open("data2.csv", "r")
data = f.readlines()
f.close()

data = data[1:]
antall_dager = len(data)/24

totalt_forbruk = 0

max_forbruk = 0
max_index = 0

#Eksempel på hvordan formatere og analysere
# dataen fra en liste
for i in range(len(data)):
    data[i] = data[i].strip()
    data[i] = data[i].split(";")
    totalt_forbruk += float(data[i][2])

    if float(data[i][2]) > max_forbruk:
        max_forbruk = float(data[i][2])
        max_index = i

tidspunkt_max_forbruk = data[max_index][0]
gjennomsnitt = totalt_forbruk/len(data)


f = open("filnavn.txt", "w")
f.write("test")
f.close()

print(antall_dager, "dager")
print(gjennomsnitt, "forbruk per time")
print(tidspunkt_max_forbruk, "er tidspunkt for max forbruk")
