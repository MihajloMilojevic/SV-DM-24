import math

print("Razvijanje binomne formule: (a+b)^n")
while True:
    try:
        a=int(input("Unesite a:"))
        break
    except ValueError:
        print("Niste uneli ceo broj!")

while True:
    try:
        b=int(input("Unesite b:"))
        break
    except ValueError:
        print("Niste uneli ceo broj!")

while True:
    try:
        n=int(input("Unesite n:"))
        if n<=0:
            print("n mora biti pozitivan ceo broj!")
            continue
        break
    except ValueError:
        print("Niste uneli ceo broj!")

print("Razvoj binomne formule:")

opsti_razvoj = []
razvoj = []
medjukoraci = []
vrednost = 0

for k in range(n + 1):
    koeficijent = math.comb(n, k)
    
    # Pravimo izraz u obliku koeficijent * a^(n-k) * b^k

    clan_opste= f"{koeficijent} * a^{n - k} * b^{k}"
    opsti_razvoj.append(clan_opste)

    if a<0 and b<0:
        clan = f"{koeficijent} * ({a})^{n - k} * ({b})^{k}"
    elif a<0:
        clan = f"{koeficijent} * ({a})^{n - k} * {b}^{k}"
    elif b<0:
        clan = f"{koeficijent} * {a}^{n - k} * ({b})^{k}"
    else:
        clan = f"{koeficijent} * {a}^{n - k} * {b}^{k}"
    razvoj.append(clan)
    
    # Izračunavamo vrednost člana
    clan_vrednost = koeficijent * (a ** (n - k)) * (b ** k)
    vrednost += clan_vrednost
    
    medjukoraci.append(str(clan_vrednost))

# Prikazujemo razvoj i međukorake u obliku stringova
razvoj_str = " + ".join(razvoj)
medjukoraci_str = " + ".join(medjukoraci)
    
print("Opšti oblik binomne formule:")
print(f"(a + b)^{n} = "+" + ".join(opsti_razvoj))

print("Razvoj za unete vrednosti:")
print(f"({a} + {b})^{n} = {razvoj_str}")
print(f"Međukorak: {medjukoraci_str}")
print(f"Vrednost izraza: {vrednost}")
