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
        m=int(input("Unesite broj elemenata koji se uredjuje(ujedno i broj ponavljanja svakog elementa):"))
        if m<=0:
            print("Broj elemenata uredjenja mora biti pozitivan ceo broj!")
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
#formula: l^m
broj=l**m
print("Broj m-permutacija multiskupa: "+str(broj))

resenja=[]

def generisi_permutacije(m, trenutna_permutacija):
    if len(trenutna_permutacija) == m:
        resenja.append(tuple(trenutna_permutacija))  # Čuvamo trenutnu permutaciju
        return

    for element in skup:
        trenutna_permutacija.append(element)  # Dodajemo element
        generisi_permutacije(m, trenutna_permutacija)
        trenutna_permutacija.pop()  # Uklanjamo poslednji element za sledeći izbor


generisi_permutacije(m, [])

print("Generisane m-permutacije multiskupa:")
for permutacija in resenja:
    print(permutacija)