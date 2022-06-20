import matplotlib.pyplot as plt
import pandas as pd
import math
# Import von notwendigen Packages zum Bearbeiten des Datensatzes
# Erstellung der Kürzel "pd" und "plt" für einen effizienteren Code
file = pd.read_csv("Datensatz/06-Kassendaten.csv", sep=";", decimal=".")

(file.corr())
# Berechnung aller Korrelationen
cor = file.Bezahlungsart.corr(file.Betrag)
# Eingrenzung aller Korrelationen mit Bezahlungsart und Betrag
if cor > 0.5:
    print("Korrelationskoeffizient:",cor, "Es handelt sich dabei um eine starken Zusammenhang")

elif cor > 0.3:
    print("Korrelationskoeffizient:",cor, "Es handelt sich dabei um eine mittleren Zusammenhang")

elif cor > 0.1:
    print("Korrelationskoeffizient:",cor, "Es handelt sich dabei um eine schwachen Zusammenhang")
# if und elif Verschachtelungen zeigen die Stärke der Korrelationen auf