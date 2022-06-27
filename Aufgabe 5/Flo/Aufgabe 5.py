import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
import math
# Import von notwendigen Packages zum Bearbeiten des Datensatzes
# Erstellung der Kürzel "pd" und "plt" für einen effizienteren Code
file = pd.read_csv("Datensatz/06-Kassendaten.csv", sep=";", decimal=".")

x = file['Betrag']
y = file['Zufriedenheit']

res = stats.linregress(x, y)

print(f"R-squared: {res.rvalue**2:.6f}")

plt.plot(x, y, 'o', label='original data')
plt.plot(x, res.intercept + res.slope*x, 'r', label='Regressionsgerade')
plt.legend()
plt.show()
