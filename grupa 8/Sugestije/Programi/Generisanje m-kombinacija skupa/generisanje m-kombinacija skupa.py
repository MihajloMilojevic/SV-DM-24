import math

while True:
    try:
        n=int(input("Unesite velicinu skupa:"))
        if n<=0:
            print("Velicina skupa mora biti pozitivan ceo broj!")
            continue
        break
    except ValueError:
        print("Niste uneli ceo broj!")

while True:
    try:
        m=int(input("Unesite broj elemenata kombinacije:"))
        if m<=0:
            print("Broj elemenata kombinacije mora biti pozitivan ceo broj!")
            continue
        break
    except ValueError:
        print("Niste uneli ceo broj!")

skup=[]
for i in range(n):
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

print("Uneli ste skup: "+str(skup))
print("Resenje:")
#formula: n!/((n-m)!m!)
broj=(int)(math.factorial(n)/(math.factorial(n-m)*math.factorial(m)))
print("Broj m-kombinacija skupa: "+str(broj))

resenja=[]

def generisi_kombinacije(m, pocetak, trenutna_kombinacija, skup):
    if len(trenutna_kombinacija) == m:
        resenja.append(tuple(trenutna_kombinacija))
        return
    
    for i in range(pocetak, len(skup)):
        trenutna_kombinacija.append(skup[i])
        generisi_kombinacije(m, i + 1, trenutna_kombinacija, skup)
        trenutna_kombinacija.pop()

generisi_kombinacije(m, 0, [], skup)

print("Generisane m-kombinacije skupa:")
for kombinacija in resenja:
    print(kombinacija)