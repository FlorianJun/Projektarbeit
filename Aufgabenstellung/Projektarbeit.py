#Nr.1 Zeile 2-5
import pandas as pd
file = pd.read_csv("06-Kassendaten.csv", sep=";", decimal=".")
print(file.head(15))
print("Anzahl der Datensätze insgesamt:", len(file))

#Nr.2 Zeile 7-17
import pandas as pd
file = pd.read_csv("06-Kassendaten.csv", sep=";", decimal=".")
data = file[["Betrag", "Bezahlungsart", "Zufriedenheit"]]
print(round(data.mean(), 2))
print(round(data.mode(), 2))
mean = repr(round(data.mean(), 2))
txt = open("Auswertungsergebnisse.txt", "w")
mode = repr(round(data.mode(), 2))
txt.write(mean + "\n" + "\n" + mode)
txt.close()

#Nr.3 Zeile 20-44
import pandas as pd
import matplotlib.pyplot as plt
file = pd.read_csv("06-Kassendaten.csv", sep=";", decimal=".")
plt.subplot(121)
xwert = ["K1", "K2", "K3", "K4", "K5", "K6", "K7", "K8"]
K1 = file.loc[file["Kassennummer"] == 1].count()[0]
K2 = file.loc[file["Kassennummer"] == 2].count()[0]
K3 = file.loc[file["Kassennummer"] == 3].count()[0]
K4 = file.loc[file["Kassennummer"] == 4].count()[0]
K5 = file.loc[file["Kassennummer"] == 5].count()[0]
K6 = file.loc[file["Kassennummer"] == 6].count()[0]
K7 = file.loc[file["Kassennummer"] == 7].count()[0]
K8 = file.loc[file["Kassennummer"] == 8].count()[0]
ywert = [K1, K2, K3, K4, K5, K6, K7, K8]
plt.bar(xwert, ywert)
plt.xlabel("Kassennummer")
plt.ylabel("häufigkeit")
plt.title("Kassennummer")
plt.subplot(122)
B = file["Bezahlungsart"]
y = B.value_counts("1")
labels = ["Bezahlungsart1", "Bezahlungsart2"]
plt.pie(y, labels=labels, autopct="%.2f %%")
plt.title("Bezahlungsart")
plt.show()

#Nr.4 Zeile 47-64
import pandas as pd
file = pd.read_csv("06-Kassendaten.csv", sep=";", decimal=".")
corr = (file["Betrag"].corr(file["Zufriedenheit"]))
print("Der Korrelationskoeffizient beträgt :", corr)
if -0.3 < corr < 0.3:
    print("kein signifikanter, linearer Zusammenhang")
elif 0.3 <= corr < 0.5 and corr > 0:
    print("schwach positiver linearer Zusammenhang")
elif 0.5 <= corr < 0.8 and corr > 0:
    print("mittelstarker positiver linearer Zusammenhang")
elif corr >= 0.8:
    print("starker positiver linearer Zusammenhang")
elif -0.5 < corr >= -0.3 and corr < 0:
    print("schwach negativer linearer Zusammenhang")
elif -0.8 < corr >= -0.5 and corr < 0:
    print("mittelstarker negativer linearer Zusammenhang")
elif corr <= -0.8:
    print("starker negativer linearer Zusammenhang")

#Nr.5 Zeile 67-78
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
file = pd.read_csv("06-Kassendaten.csv", sep=";", decimal=".")
x = file["Betrag"]
y = file["Zufriedenheit"]
plt.scatter(x, y)
plt.ylabel("Zufriedenhgeit")
plt.xlabel("Betrag in Euro")
b, a = np.polyfit(x, y, deg=1)
plt.plot(x, a + b * x, color="k")
plt.show()