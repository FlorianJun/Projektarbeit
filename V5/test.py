import pandas as pd
file = pd.read_csv("Dataset/Whg-Berlin-2016.csv", sep=";", decimal=".")

#print(file [["Fläche", "Miete"]] [0:6].mean())

#print(file [["Nummer", "Lage"]] [0:100].std()

#data = file[(file["Lage"] == 1)]
#print("Durschnittliche Miethöhe (Lage 1): "), round(data ["Miete"].mean() 2))

data = file[(file["Lage"] == 1)]
print("Durschnitliche Miethöhe: "), (data["Miete"].mean())

data = file[(file["Lage"] == 2)]
print(data["Miete"].mean())

data = file[(file["Lage"] == 3)]
print(data["Miete"].mean())

