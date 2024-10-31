def pascal_triangle(n):
    # Kreiramo praznu listu koja će čuvati redove Pascalovog trougla
    triangle = []
    
    # Petlja koja prolazi kroz svaki red do n
    for i in range(n):
        # Prvi i poslednji elementi svakog reda su 1
        row = [1] * (i + 1)
        
        # Popunjavamo elemente između prvog i poslednjeg u svakom redu
        for j in range(1, i):
            # Suma elemenata iznad trenutnog u prethodnom redu
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        
        # Dodajemo izgrađeni red u trougao
        triangle.append(row)
    
    return triangle

# Funkcija za unos sa proverom ispravnosti
def get_positive_integer():
    while True:
        try:
            # Tražimo unos od korisnika
            n = int(input("Unesite broj redova (pozitivan ceo broj): "))
            
            # Proveravamo da li je broj pozitivan
            if n > 0:
                return n
            else:
                print("Greška: Unesite pozitivan ceo broj!")
        except ValueError:
            # Ispisuje poruku ako unos nije ceo broj
            print("Greška: Unos mora biti ceo broj!")

# Funkcija za centrirani ispis Pascalovog trougla
def print_centered_triangle(triangle):
    max_width = len(" ".join(map(str, triangle[-1])))  # Maksimalna širina poslednjeg reda
    for row in triangle:
        row_str = " ".join(map(str, row))
        print(row_str.center(max_width))  # Centrirani ispis svakog reda

# Glavni deo programa
n = get_positive_integer()
triangle = pascal_triangle(n)
print_centered_triangle(triangle)
