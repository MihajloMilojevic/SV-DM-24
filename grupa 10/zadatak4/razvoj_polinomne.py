from math import factorial
from itertools import combinations_with_replacement
from collections import Counter

def multinomial_coefficient(exponents):
    # Računanje multinomnog koeficijenta
    # Multinomni koeficijent se koristi za određivanje broja načina za raspodelu eksponenata
    # Koristi se formula: k! / (k1! * k2! * ... * kn!), gde su k1, k2, ..., kn eksponenti
    k = sum(exponents)
    numerator = factorial(k)  # Faktorijal zbira eksponenata
    denominator = 1
    # Faktorijali eksponenata koriste se za računanje u nazivniku
    for count in Counter(exponents).values():
        denominator *= factorial(count)  # Računa faktorijale za svaku grupu eksponenata
    for exp in exponents:
        denominator *= factorial(exp)  # Dodaje faktorijale za pojedinačne eksponente
    return numerator // denominator  # Vraća rezultat deljenja

def polynomial_expansion(variables, k):
    n = len(variables)  # Broj promenljivih
    terms = []  # Lista u kojoj će se čuvati svi monomi rezultata
    
    # Pronalazak svih mogućih kombinacija eksponenata za dat broj promenljivih i stepen
    for exponents in combinations_with_replacement(range(k + 1), n):
        if sum(exponents) == k:
            # Ako je zbir eksponenata jednak stepenu, računamo koeficijent
            coeff = multinomial_coefficient(exponents)
            # Kreiranje monoma sa odgovarajućim eksponentima i promenljivim
            term = f"{coeff}" + "".join(
                f"({variables[i]})^{exponents[i]}" if exponents[i] > 0 else ""
                for i in range(n)
            )
            terms.append(term)  # Dodavanje monoma u listu rezultata
    
    # Kombinovanje monoma u jedan string koji predstavlja rezultat
    result = " + ".join(terms)
    return result

def get_input():
    while True:
        try:
            # Unos broja promenljivih i provera da li je unos validan
            n = int(input("Unesite broj promenljivih (pozitivan ceo broj): "))
            if n <= 0:
                print("Broj promenljivih mora biti pozitivan.")
                continue
            
            # Prikupljanje jedinstvenih imena promenljivih
            variables = []
            for i in range(n):
                while True:
                    var_name = input(f"Unesite ime promenljive {i + 1}: ")
                    if var_name.isdigit():
                        print("Ime promenljive ne sme biti broj. Pokušajte ponovo.")
                    elif var_name in variables:
                        print("Ime promenljive mora biti jedinstveno. Pokušajte ponovo.")
                    else:
                        variables.append(var_name)  # Dodavanje validnog imena u listu
                        break
            
            # Unos stepena polinoma i provera validnosti
            k = int(input("Unesite stepen polinoma (nenegativan ceo broj): "))
            if k < 0:
                print("Stepen mora biti nenegativan.")
                continue
            return variables, k  # Vraćanje liste promenljivih i stepena polinoma
        except ValueError:
            print("Unos nije validan. Molimo unesite ceo broj.")

# Glavni deo programa
variables, k = get_input()  # Prikupljanje unosa korisnika
print(f"({' + '.join(variables)})^{k} = {polynomial_expansion(variables, k)}")  # Prikaz rezultata
