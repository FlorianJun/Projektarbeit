import matplotlib.pyplot as plt
import pandas as pd


file = pd.read_csv("Dataset/Whg-Berlin-2016.csv", sep=";", decimal=".")
daten = file["Miete"]
plt.plot(daten, "r:")
plt.xlabel("Anzahl der Wohnung")
plt.ylabel("Mietehöhe")
# plt.show()


g = file[["Zimmeranzahl", "Fläche", "Miete"]].mean()
f = "Zimmeranzahl", "Fläche", "Miete"

plt.bar(f, g)
plt.xlabel("Metrische Werte")
plt.ylabel("Mittelwerte")
plt.title("Diagramm")
# plt.show()

# h = file[["Zimmeranzahl", "Fläche", "Miete"]].mean()
# f = "Zimmeranzahl", "Fläche", "Miete"

fig, ax= plt.subplots(1,2, figsize=(9,9))
ax[0].bar(f, g)
ax[1].bar(f, g)
# plt.show()

plt.subplot(2,1,2) #zeilen,spalten
plt.plot(daten, "r:")
plt.xlabel("Anzhal Wohnungen")
plt.ylabel("Miethöhe")

plt.subplot(2,1,2) #zeilen,spalten
plt.plot(daten, "r:")
plt.xlabel("Anzhal Wohnungen")
plt.ylabel("Miethöhe")
plt.show()