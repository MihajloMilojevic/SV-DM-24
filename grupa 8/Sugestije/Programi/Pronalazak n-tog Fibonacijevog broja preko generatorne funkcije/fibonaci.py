import sympy as sp#biblioteka za simbolicke izraze i simbolicke operacije, ovde se korisiti za razvoj u red

def fibonaci(n):
    # Definisanje promenljive x
    x = sp.symbols('x')#oznaka za promenljivu
    gf = 1 / (1 - x - x**2)#generativna funkcija za fibonacijev niz

    print("Generativna funkcija za Fibonacijeve brojeve:")
    print(f"F(x) = {gf}")

    # Ekspandovanje generativne funkcije u seriju do n-tog člana
    serija = sp.series(gf, x, 0, n+1)#od 0 do n+1 bez n+1-tog clana
    
    print("Ekspandovana serija do n-tog člana:")
    print(serija)

    # Uzimanje n-tog člana
    rezultat = serija.coeff(x, n)
    
    return rezultat

# Izračunavanje 10-tog fibonacijevog broja
try:
    n = int(input("Unesite n: "))
    print(f"10-ti Fibonacijev broj je: {fibonaci(n)}\n")
except ValueError:
    print("Neispravan unos.")