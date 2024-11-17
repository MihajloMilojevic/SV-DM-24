a=int(input("Unesite prvi član niza: "))
print("Moguci unosi su a(n) = a(n-1) + 'broj' i a(n) = 'broj' * a(n-1)")
formula=input("Unesite rekurentnu relaciju za niz: ")
n= int(input("Unesite broj članova niza: "))

niz=[a]

tokeni=formula.split(" ")

if tokeni[0]=="a(n)":
    if tokeni[1]=="=":
        if tokeni[2]=="a(n-1)":
            if tokeni[3]=="+":
                try:
                    broj=int(tokeni[4])
                    for i in range(1,n):
                        a+=broj
                        niz.append(a)
                except ValueError:
                    print("Neispravna formula!")
            else:
                print("Neispravna formula!")
        else:
            try:
                broj=int(tokeni[2])
                for i in range(1,n):
                    a*=broj
                    niz.append(a)
            except ValueError:
                print("Neispravna formula!")
    else:
        print("Neispravna formula!")
else:
    print("Neispravna formula!")

print(niz)
