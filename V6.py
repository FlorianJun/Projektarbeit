import matplotlib.pyplot as plt
import pandas as pd

#file = pd.read_csv("Dataset/Whg-Berlin-2016.csv", sep=";", decimal=".")
#daten = file ["Miete"][0:19]
#plt.plot(daten, "r:")
#plt.xlabel("Anzahl der Wohnung")
#plt.ylabel("Mietehöhe")
#plt.show()


#(daten["Miete"].mean())

ywerte = [4, 7, 1, 9, 5, 2, 8]
xwerte = [1, 2, 3, 4, 5, 6, 7]
#miete = file["Miete"]
plt.bar(xwerte, ywerte)
plt.show()




#Aufgabe 2 & 3 machen