import pandas as pd
# pandas wird importiert um die csv datei auslesen und mit ihr arbeiten zu können
# pd wird durch das "as" als kürzel festgelegt um auf auf pandas zuzugreifen
file = pd.read_csv("06-Kassendaten.csv", sep=";", decimal=".")
# die csv datei wird ausgelesen und als dataframe "file" gespeichert
corr = (file["Betrag"].corr(file["Zufriedenheit"]))
# über die variable "corr" lässt sich nun auf den korrelationskoeffizienten der merkmale "Betrag" und
# "Zufriedenheit" zugreifen
print("Der Korrelationskoeffizient beträgt :", corr)
# der korrelationskoeffizient wird ausgegeben
if -0.3 > corr < 0.3:
    print("kein signifikanter, linearer Zusammenhang")
elif 0.3 <= corr < 0.5:
    print("schwach positiver linearer Zusammenhang")
elif 0.5 <= corr < 0.8:
    print("mittelstarker positiver linearer Zusammenhang")
elif corr >= 0.8:
    print("starker positiver linearer Zusammenhang")
elif -0.5 < corr >= -0.3:
    print("schwach negativer linearer Zusammenhang")
elif -0.8 < corr >= -0.5:
    print("mittelstarker negativer linearer Zusammenhang")
elif corr <= -0.8:
    print("starker negativer linearer Zusammenhang")
# über if und elif wird definiert wie relevant die korrelation zwischen den merkmalen ist
# und die interpretation wird mittels print befehl ausgegeben
# (!!! eigemtlich nicht nötig, da das programm nur für den spezifischen Datensatz 06-Kassendaten funktionieren muss !!!)
