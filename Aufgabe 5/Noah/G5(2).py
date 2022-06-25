import pandas as pd
# pandas wird importiert um die csv datei auslesen und mit ihr arbeiten zu können
# pd wird durch das "as" als kürzel festgelegt um auf auf pandas zuzugreifen
import numpy as np
# numpy wird importiert um daten zu verarbeiten
# np wird durch das "np" als kürzel festgelegt um auf numpy zuzugreifen
import matplotlib.pyplot as plt
# matplotlib.pyplot wird importiert um merkmale aus der csv datei zu visualisieren
# plt wird durch das "as" als kürzel festgelegt um auf matplotlib.pyplot zuzugreifen
file = pd.read_csv("06-Kassendaten.csv", sep=";", decimal=".")
# die csv datei wird ausgelesen und als dataframe "file" gespeichert
x = file["Betrag"]
# über x als variable ist es nun möglich nur auf die spalte "Betrag" aus dem Dataframe zuzugreifen
y = file["Zufriedenheit"]
# über y als variable ist es nun möglich nur auf die spalte "Zufriedenheit" aus dem Dataframe zuzugreifen
plt.scatter(x, y)
# ein scatterplot zu den Merkmalen "Zufriedenheit" und "Betrag" wird erstellt
plt.ylabel("Zufriedenhgeit")
plt.xlabel("Betrag in Euro")
# x und y achse werden benannt
b, a = np.polyfit(x, y, deg=1)
# die funktion berechnet die steigung (b) und einen schnittpunkt (a) für die Regressionsgerade
plt.plot(x, a + b * x, color="k")
# dem Scatter Plot wird nun eine Regressionsgerade hinzugefügt
plt.show()
