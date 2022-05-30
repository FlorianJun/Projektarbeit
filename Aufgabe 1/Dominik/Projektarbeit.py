import pandas as pd

file = pd.read_csv("06-Kassendaten.csv", sep=";", decimal=".")
print(file[["TA-Kennzeichen","Betrag","Kassennummer","Bezahlungsart","Zufriedenheit"]][1:16])
