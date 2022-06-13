import pandas as pd
# pandas wird importiert um die csv datei auslesen und mit ihr arbeiten zu können
# pd wird durch das "as" als kürzel festgelegt um auf auf pandas zuzugreifen
import matplotlib.pyplot as plt
# matplotlib.pyplot wird importiert um merkmale aus der csv datei zu visualisieren
# plt wird durch das "as" als kürzel festgelegt um auf matplotlib.pyplot zuzugreifen
file = pd.read_csv("06-Kassendaten.csv", sep=";", decimal=".")
# die csv datei wird ausgelesen und als dataframe "file" gespeichert
plt.subplot(121)
# duch plt.subplot geben wir an, dass mehrere diagramme ausgegeben werden sollen
# die erste 1 in der klammer steht für die anzahl der reilen, die 2 steht dafür, dass 2 diagramme pro reihe
# ausgegeben werden sollen und die letzte 1 steht dafür, dass das folgende diagramm das erste (das linke) werden soll
xwert = ["K1", "K2", "K3", "K4", "K5", "K6", "K7", "K8"]
# die x-werte des diagramms werden benannt
K1 = file.loc[file["Kassennummer"] == 1].count()[0]
K2 = file.loc[file["Kassennummer"] == 2].count()[0]
K3 = file.loc[file["Kassennummer"] == 3].count()[0]
K4 = file.loc[file["Kassennummer"] == 4].count()[0]
K5 = file.loc[file["Kassennummer"] == 5].count()[0]
K6 = file.loc[file["Kassennummer"] == 6].count()[0]
K7 = file.loc[file["Kassennummer"] == 7].count()[0]
K8 = file.loc[file["Kassennummer"] == 8].count()[0]
# der count befehl zählt wie häufig die einzelnen kassennummern im datensatz vorkommen
ywert = [K1, K2, K3, K4, K5, K6, K7, K8]
# die erhobenen daten sind die y-werte des diagramms
plt.bar(xwert, ywert)
# ein balkendiagramm mit den zuvor definierten x und y werten soll ausgegeben werden
plt.xlabel("Kassennummer")
# die x-achse bekommt das label "Kassennummer"
plt.ylabel("häufigkeit")
# die y-achse bekommt das label "häufigkeit"
plt.title("Kassennummer")
# das diagramm bekommt den titel "Kassennummer"
plt.subplot(122)
# die dritte ziffer gibt an, dass es sich bei dem folgenden diagramm um das zweite in der ersten reihe handelt
B = file["Bezahlungsart"]
# B wird als Variable für das Merkmal Bezahlungsart der csv datei festgelegt
y = B.value_counts("1")
# y als variable greift auf die häufigkeit der verschiedenen werte des merkmals Bezahlungsart zu
labels = ["Bezahlungsart1", "Bezahlungsart2"]
# im diagramm sollen die beiden werte als "Bezahlungsart1" und "Bezahlungsart2" beschriftet werden
plt.pie(y, labels=labels, autopct="%.2f %%")
# es soll ein kuchendiagramm ausgegeben werden, dass die Daten B1 und B2 betrachtet und in prozent angibt wie häufig
# welche bezahlungsmethode verwendet wurde
plt.title("Bezahlungsart")
# das diagramm bekommt den titel "Bezahlungsart"
plt.show()
# die beiden diagramme werden nebeneinander ausgegeben
