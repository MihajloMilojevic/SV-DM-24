from itertools import combinations_with_replacement
import math
from collections import Counter

print("Razvijanje polinomne formule: (x1 + x2 + ... + xm)^n")

while True:
    try:
        m = int(input("Unesite m (broj sabiraka u polinomnoj formuli): "))
        if m <= 1:
            print("m mora biti pozitivan ceo broj veći od 1!")
            continue
        break
    except ValueError:
        print("Niste uneli ceo broj!")

sabirci = []
for i in range(m):
    while True:
        try:
            x = int(input(f"Unesite x{i + 1}: "))
            sabirci.append(x)
            break
        except ValueError:
            print("Niste uneli ceo broj!")

while True:
    try:
        n = int(input("Unesite n: "))
        if n <= 0:
            print("n mora biti pozitivan ceo broj!")
            continue
        break
    except ValueError:
        print("Niste uneli ceo broj!")

opsti_oblik = "(" + " + ".join([f"x{i + 1}" for i in range(m)]) + f")^{n}"
realan_oblik = "(" + " + ".join([str(sabirci[i]) for i in range(m)]) + f")^{n}"
print(f"Uneli ste polinomnu formulu: {opsti_oblik}")
print("Razvoj polinomne formule:")

opsti_razvoj = []
razvoj = []
medjukoraci = []
vrednost = 0

# Generisanje svih članova polinomnog razvoja koristeći kombinacije sa ponavljanjem
indeksi = combinations_with_replacement(range(m), n)#svaka cifra je neki od sabiraka a broj pojavljivanja te cifre je njen stepen

for kombinacija in indeksi:
    # Prebrojavanje broja pojavljivanja svakog indeksa
    brojevi = Counter(kombinacija)
    koeficijent = math.factorial(n) // math.prod([math.factorial(brojevi[i]) for i in range(m)])#koeficijent je n!/(a1!*a2!*...*am!) gde su a1,a2,...,am stepeni sabiraka

    # Pravimo izraz u obliku koeficijent * x1^a1 * x2^a2 * ... * xm^am
    clan_opste = f"{koeficijent} * " + " * ".join([f"x{i + 1}^{brojevi[i]}" for i in range(m) if brojevi[i] > 0])
    opsti_razvoj.append(clan_opste)

    clan = f"{koeficijent} * " + " * ".join([f"{sabirci[i]}^{brojevi[i]}" for i in range(m) if brojevi[i] > 0])
    razvoj.append(clan)

    clan_vrednost = koeficijent * math.prod([sabirci[i] ** brojevi[i] for i in range(m)])
    vrednost += clan_vrednost
    medjukoraci.append(str(clan_vrednost))

razvoj_str = " + ".join(razvoj)
medjukoraci_str = " + ".join(medjukoraci)

print("Opšti oblik polinomne formule:")
print(f"{opsti_oblik} = " + " + ".join(opsti_razvoj))

print("Razvoj za unete vrednosti:")
print(f"{realan_oblik} = {razvoj_str}")
print(f"Međukorak: {medjukoraci_str}")
print(f"Vrednost izraza: {vrednost}")