import pandas as pd
# pandas wird importiert um die csv datei auslesen und mit ihr arbeiten zu können
# pd wird durch das "as" als kürzel festgelegt um auf auf pandas zuzugreifen
file = pd.read_csv("06-Kassendaten.csv", sep=";", decimal=".")
# die csv datei wird ausgelesen und als dataframe "file" gespeichert
data = file[["Betrag", "Bezahlungsart", "Zufriedenheit"]]
# über data als variable ist es nun möglich nur die metrischen merkmale des datensatzes zu betrachten
print(data.mean())
print(data.mode())
# die ergebnisse des arithmetischen mittels und des modalwertes für die metrischen merkmale der datei werden ausgegeben
txt = open("Auswertungsergebnisse.txt", "x")
# mit txt = open erlaubt man dem Programm auf ein File zuzugreifen in diesem fall über das kürzel txt
# der modus x erlaubt es eine neue textdatei mit dem zuvor gewählten namen zu erstellen
mean = repr(data.mean())
mode = repr(data.mode())
# mean und mode werden durch repr repräsentanten für die ergebnisse
# dies ist notwendig, da der write befehl nur string eingaben und keine normalen variablen akzeptiert
txt.write(mean + "\n" + "\n" + mode)
# mit txt.write lässt sich der inhalt definieren, der in der neuen textdatei enthalten sein soll
# " + "\n" + "\n" " zwischen den ergebnissen sorgt in der textdatei zweimal für einen zeilensprung
# damit ist die textdatei etwas übersichtlicher, da die beiden ergebnisse voneinander getrennt werden
txt.close()
# fh.close signalisiert dem programm, dass es nicht länger auf die textdatei zugreifen soll
