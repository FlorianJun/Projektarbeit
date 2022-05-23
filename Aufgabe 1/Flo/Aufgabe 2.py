a = "j"

while a == "j":
    jahreszahl = int(input("Geben Sie ihre Jahreszahl ein: "))
    if jahreszahl % 4 == 0 and jahreszahl % 100 != 0:
        print("Es besteht ein Schaltjahr")
    elif jahreszahl % 400 == 0:
        print("Es besteht ein Jahrhundert Schlatjahr")
    elif jahreszahl % 100 != 0:
        print("Es besteht kein Schaltjahr")
    a = input("Möchten sie ein weiteres Jahr überpfrüfen? (j/n): ")
