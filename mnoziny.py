pythoon_devs = {"Pepa", "Jirka", "honza", "Marek", "Petr", "Roman"}
java_devs = {"Roman", "Petr", "karel", "Lucie"}

vsichni_devs = pythoon_devs - java_devs
print("Všichni vývojáři (rozdíl):", vsichni_devs)

polyglot_devs = pythoon_devs & java_devs
print("Vývojáři, kteří ovládjí oba jazyky:", polyglot_devs)