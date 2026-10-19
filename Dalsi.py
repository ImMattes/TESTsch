# Slovníky asi

kontakt = {
    "jmeno": "Jan",
    "Prijmeni": "Novák",
    "vek": 30,
    "telefon": 123456
}

print ("původní kontakty:", kontakt)

print("Jmeno:", kontakt["jmeno"])

kontakt["vek"] = 66
print(kontakt["vek"])

kontakt["mesto"] = "Ostrava"
print(kontakt)

telefon = kontakt.get("telefon")
print("Telefonní číslo:", telefon)