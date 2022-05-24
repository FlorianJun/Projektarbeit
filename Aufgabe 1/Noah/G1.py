# pandas wird importiert um die csv datei auslesen und mit ihr arbeiten zu können
# pd wird durch das "as" als kürzel festgelegt um auf auf pandas zuzugreifen
import pandas as pd
# die csv datei wird ausgelesen und als dataframe "file" gespeichert
file = pd.read_csv("06-Kassendaten.csv", sep=";", decimal=".")
# die ersten 15 datensätze werden ausgegeben
print(file.head(15))
# die anzahl aller datensätze in der csv datei werden ausgegeben
print("Anzahl der Datensätze insgesamt:", len(file))
