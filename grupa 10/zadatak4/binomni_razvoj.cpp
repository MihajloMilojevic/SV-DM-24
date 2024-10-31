#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

// Funkcija za izračunavanje faktorijela
long long faktorijel(int n) {
    long long rezultat = 1;
    for (int i = 1; i <= n; i++) {
        rezultat *= i;
    }
    return rezultat;
}

// Funkcija za binomni koeficijent
long long binomniKoeficijent(int n, int k) {
    return faktorijel(n) / (faktorijel(k) * faktorijel(n - k));
}

// Funkcija za razvoj binomne formule sa formatiranim ispisom
void binomniRazvoj(int n, int a, int b) {
    cout << "(" << a << " + " << b << ")^" << n << " = " << endl;
    for (int k = 0; k <= n; k++) {
        long long koeficijent = binomniKoeficijent(n, k);  // Računamo binomni koeficijent

        // Lepši format ispisa sa eksplicitnim prikazom stepenova
        cout << setw(4) << koeficijent << " * " << a << "^" << setw(2) << (n - k)
             << " * " << b << "^" << setw(2) << k;

        // Dodajemo "+" između članova osim kod poslednjeg člana
        if (k < n) {
            cout << " +";
        }
        
        cout << endl;
    }
}

// Funkcija za unos validnog celog broja
int unosCelogBroja(const string& poruka) {
    int broj;
    while (true) {
        cout << poruka;
        if (cin >> broj) {  // Provera uspešnosti unosa
            break;
        } else {
            cout << "Greška: Molimo unesite ceo broj.\n";
            cin.clear(); // Resetovanje cin stanja
            cin.ignore(10000, '\n'); // Ignorisanje preostalih karaktera u redu
        }
    }
    return broj;
}

int main() {
    // Unos sa proverom za stepen n, vrednosti a i b
    int n = unosCelogBroja("Unesite stepen n: ");
    int a = unosCelogBroja("Unesite a: ");
    int b = unosCelogBroja("Unesite b: ");

    // Pozivanje funkcije za razvoj binomne formule
    binomniRazvoj(n, a, b);
    
    return 0;
}
