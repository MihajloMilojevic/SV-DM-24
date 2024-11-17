import math
from typing import Counter

while True:
    try:
        l=int(input("Unesite velicinu skupa:"))
        if l<=0:
            print("Velicina skupa mora biti pozitivan ceo broj!")
            continue
        break
    except ValueError:
        print("Niste uneli ceo broj!")

skup=[]
brojPojava=[]
for i in range(l):
    while True:
        try:
            x=int(input("Unesite element skupa:"))
            if(x in skup):
                print("Element vec postoji u skupu!")
                continue
            m=int(input("Unesite broj ponavljanja elementa:"))
            if m<=0:
                print("Broj ponavljanja elementa mora biti pozitivan ceo broj!")
                continue
            break
        except ValueError:
            print("Niste uneli ceo broj!")
    skup.append(x)
    brojPojava.append(m)

multiskup=[]

for i in range(l):
    for j in range(brojPojava[i]):
        multiskup.append(skup[i])

print("Uneli ste multiskup: "+str(multiskup))
print("Resenje:")
#formula: (m1+m2+...+ml)!/(m1!*m2!*...*ml!)
broj=1
zbir=0
faktorijel=1
proizvod=1
for i in range(l):
    zbir+=brojPojava[i]
    faktorijel=1
    for j in range(1,brojPojava[i]+1):
        faktorijel*=j
    proizvod*=faktorijel
broj=math.factorial(zbir)//proizvod

print("Broj permutacija multiskupa: "+str(broj))

resenja=[]

def generisi_permutacije_multiskupa(multiskup, trenutna_permutacija, dostupni):
    if sum(dostupni.values()) == 0:  # Kada nema dostupnih elemenata
        resenja.append(tuple(trenutna_permutacija.copy()))  # Čuvamo trenutnu permutaciju
        return

    for element in dostupni:
        if dostupni[element] > 0:  # Ako je element dostupan
            trenutna_permutacija.append(element)  # Dodajemo element
            dostupni[element] -= 1  # Smanjujemo broj dostupnih
            generisi_permutacije_multiskupa(multiskup, trenutna_permutacija, dostupni)
            trenutna_permutacija.pop()
            dostupni[element] += 1

# Broj pojavljivanja za generisanje
dostupni = Counter(multiskup)

# Pozivamo funkciju za generisanje permutacija
generisi_permutacije_multiskupa(multiskup, [], dostupni)

print("Generisane permutacije multiskupa:")
for permutacija in resenja:
    print(permutacija)