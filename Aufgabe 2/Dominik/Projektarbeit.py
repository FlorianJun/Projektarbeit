import pandas as pd

file = pd.read_csv("06-Kassendaten.csv", sep=";", decimal=".")
print(file[["TA-Kennzeichen","Betrag","Kassennummer","Bezahlungsart","Zufriedenheit"]][1:16])
print("Anzahl der Datensätze insgesamt:", len(file))

#Nr.2
data1 = file["Betrag"].mean()
x = round(data1,2)
print(x)
# .mean berechnet arithmetisches Mittel

data2 = file["Kassennummer"].mode()
x = round(data2,2)
print(x)

data = ({"Durschnittlicher Betragswert":[70.22], "Am Häufigsten benutze Kasse":[6]})
df = pd.DataFrame(data)
print(df)
# mit pd.DataFrame wird neuer Datensatz erstellt

fh = open('Datensatz/Auswertungsergebnisse.txt', 'w')
# neue Textdatei "Auswertungsergebnisse.txt" wird erstellt, damit Zugriff auf fh=open
fh.write("Durschnittlicher Betragswert: 70,22 , Am Häufigsten benutze Kasse: 6")
fh.close()