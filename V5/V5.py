import pandas as pd
file = pd.read_csv("Dataset/Whg-Berlin-2016.csv", sep=";", decimal=".")

data = file[(file["Stadtteil"] == "Fri")]
print(data[["Miete", "Zimmeranzahl"]].mean())

data = file[["Fläche", "Miete", "Zimmeranzahl", "Lage"]]
print(data.corr())
x = data.corr()
print(x ["Miete"] ["Fläche"])

cZimmer = file[["Miete", "Zimmeranzahl"]].corr()["Miete"] ["Zimmeranzahl"]
cFläche = file[["Miete", "Fläche"]].corr() ["Miete"] ["Fläche"]
cLage = file[["Miete", "Lage"]].corr() ["Miete"] ["Lage"]

if abs(cZimmer) > abs(cFläche) and  abs(cZimmer > abs (cLage)):
    print("Die Miete korreliert am Stärksten mit der Zimmeranzahl")
else:
    print("Die Miete korreliert am stärksten mit der Lage")



#data = file[["Zimmeranzahl", "Miete"]]
#print(data.corr())

#data = file[(file["Lage"] == 1)]
#print(data["Miete"].mean())

#data = file[(file["Lage"] == 2)]
#print(data["Miete"].mean())

#data = file[(file["Lage"] == 3)]
#print(data["Miete"].mean())

