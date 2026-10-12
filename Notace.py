# Generátorova notace

#vytvoření sseznamu čtverců čísel od 0 do 9

ctverce = [x**2 for x in range(10)]
print(f"Čtverce čísel od 0 do 9: {ctverce}")

mocnina = []
for x in range(10):
    mocnina.append(x**2)
    print(x, x**2)

slova = ["Python", "je", "skvělý", "programovací", "jazyk"]
velka_slova = [slovo.upper() for slovo in slova]
print(f"Slova  převedená na velká písmena: {velka_slova}")