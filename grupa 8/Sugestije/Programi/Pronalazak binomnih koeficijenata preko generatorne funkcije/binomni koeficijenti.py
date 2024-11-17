import sympy as sp#biblioteka za simbolicke izraze i simbolicke operacije, ovde se korisiti za razvoj u red

def binomni_koeficijenti(n):
    # Generativna funkcija za binomne koeficijente
    x = sp.symbols('x')#oznaka za promenljivu
    gf = (1 + x)**n#generativna funkcija
    
    print("Generativna funkcija za binomne koeficijente:")
    print(f"G(x) = (1 + x)**{n}")

    # Ekspandovanje generativne funkcije u Tejlorov red
    serija = sp.series(gf, x, 0, n+1)#od 0 do n+1 bez n+1-tog clana
    
    print(f"Ekspandovana serija do {n}-tog člana:")
    print(serija)

    # izdvajanje koeficijenata iz serije i smestanje u listu
    koeficijenti = [serija.coeff(x, k) for k in range(n+1)]
    
    return koeficijenti

# Računanje svih binomnih koeficijenata za n = 5
try:
    n = int(input("Unesite n: "))
    print(f"Binomni koeficijenti za n = {n}: {binomni_koeficijenti(n)}\n")
except ValueError:
    print("Neispravan unos.")