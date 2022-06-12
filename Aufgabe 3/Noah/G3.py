import pandas as pd
# pandas wird importiert um die csv datei auslesen und mit ihr arbeiten zu können
# pd wird durch das "as" als kürzel festgelegt um auf auf pandas zuzugreifen
import matplotlib.pyplot as plt
# matplotlib.pyplot wird importiert um merkmale aus der csv datei zu visualisieren
# plt wird durch das "as" als kürzel festgelegt um auf matplotlib.pyplot zuzugreifen
file = pd.read_csv("06-Kassendaten.csv", sep=";", decimal=".")
# die csv datei wird ausgelesen und als dataframe "file" gespeichert
x = file["Kassennummer"]
# über x als variable ist es nun möglich nur auf die spalte "Kassennummer" aus dem Dataframe zuzugreifen
plt.subplot(121)
# duch plt.subplot geben wir an, dass mehrere diagramme ausgegeben werden sollen
# die erste 1 in der klammer steht für die anzahl der reilen, die 2 steht dafür, dass 2 diagramme pro reihe
# ausgegeben werden sollen und die letzte 1 steht dafür, dass das folgende diagramm das erste (das linke) werden soll
plt.hist(x, bins=8, edgecolor="black")
# die kassennummern werden in einem histogramm ausgegeben, dass angeben soll wie häufig sie in der datei vertreten sind
# (!!! ein histogramm ist vielleicht nicht am besten dafür geeignet evtl anderes diagramm verwenden !!!)
plt.xticks([1, 2, 3, 4, 5, 6, 7, 8])
# durch pltxticks werden die Abstände zwischen den Werten auf der x-achse definiert
plt.xlabel("Kassennummer")
# die x-achse bekommt das label "Kassennummer"
plt.ylabel("häufigkeit")
# die y-achse bekommt das label "häufigkeit"
plt.title("Kassennummer")
# das diagramm bekommt den titel "Kassennummer"
plt.subplot(122)
# die dritte ziffer gibt an, dass es sich bei dem folgenden diagramm um das zweite in der ersten reihe handelt
B1 = file.loc[file["Bezahlungsart"] == 1].count()[0]
# unter der variable B1 lässt sich nun darauf zugreifen wie oft die erste bezahlungsmethode verwendet wurde
B2 = file.loc[file["Bezahlungsart"] == 2].count()[0]
# unter der variable B1 lässt sich nun darauf zugreifen wie oft die zweite bezahlungsmethode verwendet wurde
labels = ["Bezahlungsart1", "Bezahlungsart2"]
# im diagramm sollen die beiden werte als "Bezahlungsart1" und "Bezahlungsart2" beschriftet werden
plt.pie([B1, B2], labels=labels, autopct="%.2f %%")
# es soll ein kuchendiagramm ausgegeben werden, dass die Daten B1 und B2 betrachtet und in prozent angibt wie häufig
# welche bezahlungsmethode verwendet wurde
plt.title("Bezahlungsart")
# das diagramm bekommt den titel "Bezahlungsart"
plt.show()
# die beiden diagramme werden nebeneinander ausgegeben
