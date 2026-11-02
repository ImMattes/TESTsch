# Další opisování

n = 10

while n > 0:
    print(n, end=' ')
    n -= 1               #n = n - 1 (to stejne s +)
print("konec odpočitávání")



for i in range(5):
    print (i*i)



jazyky  = ["CZ", "ANG", "PL", "RJ"]
for jazyk in jazyky:
    print("učím se jazyk", jazyk)



for y  in range(2, 10):
    for x in range (2,  y):
        print("Kontroluuju cislo", y, "dělené",  x)
        if y  % x == 0:
            break
else:
    print(y, "========= JE PRVOCISLO =======")



import random
velikost = 10
pole  =  [random.randint(1, 100) for i in range(velikost)]
print("neuspořádaná pole:", pole)

for i in range (velikost -1, 0, -1):
    for j in range (0,i):
        if pole[j] > pole[j+1]:
            pole[j], pole[j+1] = pole[j+1], pole[j]
print("sezařene pole:", pole)
