import sympy as sp#biblioteka za simbolicke izraze i simbolicke operacije, ovde se korisiti za razvoj u red

def kombinacije_sa_ponavljanjem(n, k):
    # Generativna funkcija za kombinacije sa ponavljanjem
    x = sp.symbols('x')#oznaka za promenljivu
    gf = (1 / (1 - x))**n#generativna funkcija za kombinacije sa ponavljanjem
    
    print("Generativna funkcija za kombinacije sa ponavljanjem:")
    print(f"G(x) = {gf}")

    # Ekspandovanje generativne funkcije u seriju
    series_expansion = sp.series(gf, x, 0, k+1)#od 0 do k+1 bez k+1-tog clana
    
    print(f"Ekspandovana serija do {k}-tog člana:")
    print(series_expansion)

    # Ekstraktovanje k-tog koeficijenta
    rezultat = series_expansion.coeff(x, k)#izdvajanje k-tog clana
    
    return rezultat

# Računanje broja kombinacija sa ponavljanjem
try:
    n = int(input("Unesite n: "))
    k = int(input("Unesite k: "))
    print(f"Broj kombinacija sa ponavljanjem za n = {n} i k = {k} je: {kombinacije_sa_ponavljanjem(n, k)}\n")
except ValueError:
    print("Neispravan unos.")