import math

while True:
    try:
        l=int(input("Unesite velicinu skupa:"))
        if l<=0:
            print("Velicina skupa mora biti pozitivan ceo broj!")
            continue
        break
    except ValueError:
        print("Niste uneli ceo broj!")

while True:
    try:
        m=int(input("Unesite broj elemenata u kombinaciji(ujedno i broj ponavljanja svakog elementa):"))
        if m<=0:
            print("Broj elemenata u kombinaciji mora biti pozitivan ceo broj!")
            continue
        break
    except ValueError:
        print("Niste uneli ceo broj!")

skup=[]
for i in range(l):
    while True:
        try:
            x=int(input("Unesite element skupa:"))
            if(x in skup):
                print("Element vec postoji u skupu!")
                continue
            break
        except ValueError:
            print("Niste uneli ceo broj!")
    skup.append(x)

multiskup=[]

for i in range(l):
    for j in range(m):
        multiskup.append(skup[i])

print("Uneli ste multiskup: "+str(multiskup))
print("Resenje:")
#formula: (l+m-1)!/m!(l-1)!
broj=(int)(math.factorial(l+m-1)/(math.factorial(m)*math.factorial(l-1)))
print("Broj m-kombinacija multiskupa: "+str(broj))

resenja=[]

def generisi_kombinacije(m, pocetak, trenutna_kombinacija):
    if len(trenutna_kombinacija) == m:
        resenja.append(tuple(trenutna_kombinacija))
        return
    
    for i in range(pocetak, len(skup)):
        trenutna_kombinacija.append(skup[i])
        generisi_kombinacije(m, i, trenutna_kombinacija)
        trenutna_kombinacija.pop()

generisi_kombinacije(m,0, [])

print("Generisane m-kombinacije multiskupa:")
for kombinacija in resenja:
    print(kombinacija)