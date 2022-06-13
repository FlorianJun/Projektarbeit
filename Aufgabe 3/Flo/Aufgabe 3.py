import matplotlib.pyplot as plt
import pandas as pd
import math
# Import von notwendigen Packages zum Bearbeiten des Datensatzes
# Erstellung der Kürzel "pd" und "plt" für einen effizienteren Code
file = pd.read_csv("Datensatz/06-Kassendaten.csv", sep=";", decimal=".")
daten = file["Bezahlungsart"]
kassen = file["Kassennummer"]

x = daten.value_counts("1")
y = kassen.value_counts("1")

exp_labels = ["Bezahlungsart 1", "Bezahlungsart 2"]
labels = ["1.Kasse","2.Kasse", "3.Kasse", "4.Kasse", "5.Kasse", "6.Kasse", "7.Kasse", "8.Kasse"]

fig, ax= plt.subplots(1,2, figsize=(9,9))
ax[0].pie(x, autopct= '%0.1f%%', labels=exp_labels)
ax[1].pie(y, autopct= '%0.1f%%',labels=labels)
plt.title("Häufigkeitsverteilung der Bezahlungsart   /   Häufigkeitsverteilung der Kassennummer                                                                            ")

plt.show()
