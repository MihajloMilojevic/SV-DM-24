niz=[]

print("Moguci unosi su aritmeticki, geometrijski, faktorijelski i Fibonacijev niz.")
print("Unesite niz brojeva, unesite kraj za izlaz: ")

while True:
    x = input()
    if x == "kraj" and len(niz) >= 2:
        break
    elif x == "kraj" and len(niz) < 2:
        print("Niz mora imati bar 2 elementa!")
        continue

    try:
        x = int(x)
    except ValueError:
        print("Niste uneli broj!")
        continue

    niz.append(int(x))

def provera_aritmeticki(niz):
    razlika = niz[1] - niz[0]

    for i in range(2, len(niz)):
        if niz[i] - niz[i-1] != razlika:
            return False

    return True

def provera_geometrijski(niz):
    if niz[0] == 0:
        return False
    odnos = niz[1] / niz[0]

    for i in range(2, len(niz)):
        if niz[i-1] == 0:
            return False
        if niz[i] / niz[i-1] != odnos:
            return False

    return True

def provera_faktorijel(niz):
    duzina = len(niz)
    
    faktorijel = 1
    for i in range(2, duzina+1):
        faktorijel *= i

    if niz[-1] != faktorijel:
        return False

    return True

def provera_fibonaci(niz):
    fib1 = 0
    fib2 = 1

    for i in range(2, len(niz)):
        fib1, fib2 = fib2, fib1 + fib2

    if niz[-1] != fib2:
        return False

    return True

if provera_aritmeticki(niz):
    print("Niz je aritmeticki.")
    print("Rekurentna relacija: a(n) = a(n-1) + d")
if provera_geometrijski(niz):
    print("Niz je geometrijski.")
    print("Rekurentna relacija: a(n) = a(n-1) * q")
if provera_faktorijel(niz):
    print("Niz je faktorijelski.")
    print("Rekurentna relacija: a(n) = n*(n-1)")
if provera_fibonaci(niz):
    print("Niz je Fibonacijev.")
    print("Rekurentna relacija: a(n) = F(n)")