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
        m=int(input("Unesite broj elemenata koji se uredjuje:"))
        if m<=0:
            print("Broj elemenata uredjenja mora biti pozitivan ceo broj!")
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
#formula: n(n-1)(n-2)...(n-m+1)
broj=1
for i in range(n, n-m, -1):
    broj*=i
print("Broj m-permutacija skupa: "+str(broj))

resenja=[]

def generisi_permutacije(m, trenutna_permutacija, dostupni):
    if len(trenutna_permutacija) == m:
        resenja.append(tuple(trenutna_permutacija))  # Čuvamo trenutnu permutaciju
        return

    for i in range(len(dostupni)):
        # Izbor i uklanjanje elementa
        element = dostupni[i]
        trenutna_permutacija.append(element)  # Dodajemo element
        # Kreiramo novi skup dostupnih elemenata bez trenutnog
        novi_dostupni = dostupni[:i] + dostupni[i + 1:]
        generisi_permutacije(m, trenutna_permutacija, novi_dostupni)
        trenutna_permutacija.pop()  # Uklanjamo poslednji element za sledeći izbor


generisi_permutacije(m, [],skup)

print("Generisane m-permutacije skupa:")
for permutacija in resenja:
    print(permutacija)