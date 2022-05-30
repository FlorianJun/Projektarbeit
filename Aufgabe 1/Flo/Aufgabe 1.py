import matplotlib.pyplot as plt
import pandas as pd
import math
# Import von notwendigen Packages zum Bearbeiten des Datensatzes
# Erstellung der Kürzel "pd" und "plt" für einen effizienteren Code
file = pd.read_csv("Datensatz/06-Kassendaten.csv", sep=";", decimal=".")
# Zugriff und auslesung des Datensatzes erfolgt nun über "file"
print(file.head(15))
# Ausgabe der ersten 15 datensätze
print("Anzahl der Datensätze insgesamt:", len(file))
# Ausgabe aller Datensätze
