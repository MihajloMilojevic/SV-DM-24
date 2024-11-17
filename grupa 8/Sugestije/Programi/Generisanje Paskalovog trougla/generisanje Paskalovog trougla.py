import math

while True:
    try:
        n=int(input("Unesite broj n (broj redova Paskalovog trougla):"))
        if n<=0:
            print("Broj redova mora biti pozitivan ceo broj!")
            continue
        break
    except ValueError:
        print("Niste uneli ceo broj!")

print("Paskalov trougao:")

for i in range(n):
    print(" "*(n-i-1), end="")
    for j in range(i+1):
        print(str(math.comb(i,j))+" ", end="")
    print()
