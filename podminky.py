cislo = 10
if cislo > 0:
    print("Hodnota je kladná")
elif cislo < 0:
    print("Hodnota je záporná")
else:
    print("Hodnota je nula")

vek = 20
if vek >= 16 and vek < 18:
    print("Nejsi plnoletý")
else:
    print("Jsi plnoletý")

body = 85
chceme_ho = True

if body >= 80:
    if chceme_ho:
        print("jo chceme ho")
        print("Má dost bodů.")
    else:
        print("má dost bodů")
        print("ale nechceme ho sorry")
else:
    print("nemá dost bodu")

cislo = 5

if cislo % 2 == 0:
    print("číslo je sude")
else:
    print("cislo je liche")

nakupni_kosik = []

if nakupni_kosik:
    print("kosik neni prazdny")
else:
    print("kosik je prazdny")

povoleno_ovoce = ["jablko", "banán", "pomeranč"]
moje_ovoce = "jablko"

if moje_ovoce in povoleno_ovoce:
    print(moje_ovoce.capitalize, "je povolene ovoce")
else:
    print(moje_ovoce.capitalize, "neni na seznamu povoleneho ovoce")