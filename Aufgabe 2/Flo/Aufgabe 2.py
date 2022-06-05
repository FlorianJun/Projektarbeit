import pandas as pd
import math
# Import von notwendigen Packages zum bearbeiten des Datensatzes
# Erstellung der Kürzel "pd" und "plt" für einen effizienteren Code
file = pd.read_csv("Datensatz/06-Kassendaten.csv", sep=";", decimal=".")
# Zugriff und auslesung des Datensatzes erfolgt nun über "file"
print(file.head(15))
# Ausgabe der ersten 15 datensätze
print("Anzahl der Datensätze insgesamt:", len(file))
# Ausgabe aller datensätze

# Auswahl der statitischen Kennzahlen: Molalwert (der häufigste Wert) für die Kassennummer.
# Welche Kassennummer hat am meisten geöffnet oder wir am meisten benutzt von den Kunden?
# Arithmetisches Mittel (durschnitt) für den bezahlten Geldbetrag: Wie viel Geld gibt ein Kunde im Durchscnitt aus?
# TA-Kennzeichen scheint unbrauchbar zu sein, Bezahlungsart ebenfalls? Unklar wo für 1 oder 2 stehen (Bar Zahlung/Karte?)

(file["Betrag"].mean())
betrag = (file["Betrag"].mean())
betrag = round(betrag, 2)
print(betrag)

# .mean berechnet hier das Arithmetische Mittel
# workaround für die Round Funktion. Habe es nicht anders hinbekommen, hier lässt sich noch Codezeilen sparren

(file["Kassennummer"].mode())
kassennummer = (file["Kassennummer"].mode())
kassennummer = round(kassennummer, 2)
print (kassennummer)

# .mode gibt den Modulawert aus (Am häufigsten vorkommender Wert)
# Mode Funktion für den Modulawert sorgt dafür das Name und Datentyp zusätzlich angegeben werden (redundant)
# Neben dem richtigen Modulawert wird auch noch eine 0 ausgegeben Grund unbekannt, sollte sich später beheben lassen

data = ({"Durschnittlicher Einkaufswert":[70.22], "Am Häufigsten benutze Kasse":[6]})
df = pd.DataFrame(data)

print(df)

# Erstellung eines neuen Datensatzes mit dem "pd.DataFrame" befehl, dieser wir als "data" gespeichert und ausgelesen


fh = open('Datensatz/Auswertungsergebnisse.txt', 'w')

#Erstellung einer neuen Textdatei "Auswertungsergebnisse.txt" zugriff auf diese mit "fh = open (Dateipfad)"

fh.write("Durschnittlicher Einkaufswert: 70,22 , Am Haeufigsten benutze Kasse: 6")

#Überschreibung der Textdatei mit den Werten, zunächst nur als texteingabe möglich, bei benutzung der Variablen z.B
# "Betrag" wird kein Text ins Dokument übernommen. Lässt sich später noch beheben
fh.close()