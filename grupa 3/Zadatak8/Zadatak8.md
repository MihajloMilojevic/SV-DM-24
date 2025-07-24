# Povezanost grafova - Kompletna analiza

## Uvod

U teoriji grafova, pojam povezanosti je fundamentalan za razumevanje strukture i svojstava grafova. Povezanost nam omogućava da analiziramo kako se čvorovi grafa mogu dosegnuti jedan od drugog putem grana, što ima brojne praktične primene u modelovanju realnih problema kao što su transportne mreže, komunikacione mreže, društvene mreže i mnogi drugi.

## 1. Osnovni pojmovi kretanja kroz graf

### 1.1 Šetnja (Walk)

**Definicija:** Neka je $G = (V, E, \Psi)$ multigraf. Neka su $e_1, e_2, \ldots, e_n \in E$ i $v_0, v_1, \ldots, v_n \in V$ proizvoljne grane i čvorovi sa osobinom $\Psi(e_i) = \{v_{i-1}, v_i\}$ za svako $i \in \{1, 2, \ldots, n\}$. Tada za niz:

$$v_0 e_1 v_1 e_2 v_2 \ldots e_n v_n$$

kažemo da je **$v_0v_n$-šetnja dužine $n$** u grafu $G$ između čvorova $v_0$ i $v_n$.

**Karakteristike šetnje:**
- Dozvoljeno je ponavljanje čvorova proizvoljno konačan broj puta
- Dozvoljeno je ponavljanje grana proizvoljno konačan broj puta
- Šetnja je najopštiji oblik povezanosti parova čvorova
- Za čvorove $v_0$ i $v_n$ kažemo da su **kranji čvorovi šetnje**

**Primer šetnje:**
Za graf sa čvorovima $\{a, b, c, d, f, g\}$ i odgovarajućim granama:
- $ad$-šetnja: $a e_1 b e_3 g e_6 d$
- $ac$-šetnja: $a e_2 g e_6 g e_6 d e_6 g e_7 f e_4 d e_6 g e_8 c$

### 1.2 Staza (Trail)

**Definicija:** Staza je šetnja bez ponavljanja grana, odnosno:

$$(\forall i, j \in \{1, 2, \ldots, n\})(i \neq j \Rightarrow e_i \neq e_j)$$

**Karakteristike staze:**
- Grane se ne ponavljaju
- Čvorovi se mogu ponavljati
- Svaka staza je ujedno i šetnja

### 1.3 Put (Path)

**Definicija:** Put je šetnja bez ponavljanja čvorova, odnosno:

$$(\forall i, j \in \{0, 1, \ldots, n\})(i \neq j \Rightarrow v_i \neq v_j)$$

**Karakteristike puta:**
- Čvorovi se ne ponavljaju
- Grane se automatski ne ponavljaju (jer nema ponavljanja čvorova)
- Svaki put je ujedno i staza i šetnja

**Napomena za proste grafove:** Ukoliko je graf $G$ prost graf, možemo izostaviti grane u zapisu (svaki par čvorova je incidentan sa najviše jednom granom), pa šetnju označavamo samo kao niz čvorova $v_0 v_1 \ldots v_n$.

### 1.4 Zatvorene forme

Ako su krajnji čvorovi jednaki, odnosno ako je $v_0 = v_n$, tada uvodimo dodatne pojmove:

- **Zatvorena šetnja:** šetnja dužine bar jedan sa $v_0 = v_n$
- **Kružna staza (Closed trail):** zatvorena staza
- **Kontura (Cycle/Circuit):** zatvoreni put

## 2. Povezanost čvorova

### 2.1 Definicija povezanosti

**Definicija:** Neka je $G = (V, E, \Psi)$ multigraf. Za čvorove $u$ i $v$ kažemo da su **povezani** akko:

$$(u = v) \text{ ili } (u \neq v \text{ i postoji } uv\text{-put u } G)$$

**Oznaka:** Da je čvor $u$ povezan sa čvorom $v$ označavamo sa $u \sim v$:

$$(u \sim v) \Leftrightarrow (u = v \vee (u \neq v \wedge \exists uv\text{-put u } G))$$

### 2.2 Povezanost grafa

**Definicija:** Kažemo da je graf $G$ **povezan** akko $|V| = 1$ ili za svako $u, v \in V$ važi $u \sim v$.

**Važna teorema:** Ako u grafu postoji $uv$-šetnja, onda postoji i $uv$-put.

**Dokaz:** Konstruktivan dokaz kroz eliminaciju ciklusa:

1. Uočimo čvor $v' \in \{v_0, v_1, \ldots, v_n\}$ koji se ponavlja u šetnji
2. Ako takav čvor ne postoji, onda su svi čvorovi jedinstveni i $uv$-šetnja je već put
3. Neka su $0 \leq i < j \leq n$ indeksi prvog i poslednjeg pojavljivanja čvora $v'$
4. Iz šetnje možemo izbaciti sve čvorove i grane između $v_i$ i $v_j$, transformišući šetnju:
   $$v_0 e_1 v_1 \ldots v_i e_{i+1} v_{i+1} \ldots e_j v_j e_{j+1} v_{j+1} \ldots e_n v_n$$
   u šetnju:
   $$v_0 e_1 v_1 \ldots v_i e_{j+1} v_{j+1} \ldots e_n v_n$$
5. Ponavljanjem ovog postupka eliminišemo sva višestruka pojavljivanja čvorova

## 3. Relacija ekvivalencije povezanosti

### 3.1 Teorema o ekvivalentnosti

**Teorema:** Relacija $\sim$ je relacija ekvivalencije nad skupom čvorova grafa.

**Dokaz:**

**(R) Refleksivnost:**
$$u = u \Rightarrow u \sim u$$
Sledi direktno iz definicije.

**(S) Simetričnost:**
Neka je $u \neq v$ i neka je jedan $uv$-put oblika $u e_1 v_1 e_2 \ldots e_n v$.
Tada je jedan $vu$-put oblika $v e_n \ldots e_2 v_1 e_1 u$, te kako postoji put iz $v$ u $u$, onda je $v \sim u$.

**(T) Tranzitivnost:**
Pretpostavimo da u grafu $G$ postoji $uv$-put i $vw$-put oblika:
- $u u_0 \ldots u_{i-1} v$
- $v v_0 \ldots v_{n-1} w$

Tada je:
$$u u_0 \ldots u_{i-1} v v_0 \ldots v_{n-1} w$$
jedna $uw$-šetnja u grafu, odakle sledi da je $u \sim w$.

### 3.2 Posledice ekvivalentnosti

Kako je relacija $\sim$ relacija ekvivalencije na skupu čvorova $V$ grafa $G$, ona skup $V$ deli na skup klasa ekvivalencije $V/\sim$. Svaka klasa ekvivalencije indukuje podgraf grafa $G$ koji nazivamo **komponentom povezanosti** tog grafa.

## 4. Komponente povezanosti

### 4.1 Definicija

**Komponenta povezanosti** je maksimalan povezan podgraf grafa, odnosno svaka komponenta povezanosti je podgraf koji nije sadržan ni u jednom drugom povezanom podgrafu istog grafa.

### 4.2 Broj komponenti povezanosti

**Definicija:** Broj komponenti povezanosti grafa $G$, u oznaci $\omega(G)$, jednak je broju klasa ekvivalencije u odnosu na relaciju $\sim$ (povezanosti čvorova):

$$\omega: \{G = (V, E, \Psi) | G \text{ je graf}\} \to \mathbb{N}$$
$$\omega(G) = |V_G/\sim|$$

### 4.3 Teorema o povezanosti i broju komponenti

**Teorema:** Multigraf $G = (V, E, \Psi)$ je povezan akko $\omega(G) = 1$.

**Dokaz:**
$$G \text{ je povezan} \Leftrightarrow (\forall u, v \in V)(u \sim v)$$
$$\Leftrightarrow V/\sim = \{V\} \text{ (svi čvorovi pripadaju istoj klasi ekvivalencije)}$$
$$\Leftrightarrow |V/\sim| = 1 \Leftrightarrow \omega(G) = 1$$

## 5. Teorema o minimalnom broju grana za povezanost

### 5.1 Formulacija teoreme

**Teorema:** Prost graf $G = (V, E)$ sa $n$ čvorova $(|V| = n)$ i manje od $n-1$ grana $(|E| < n-1)$ nije povezan, za $n \geq 2$.

### 5.2 Dokaz indukcijom

**Dokaz:**

**Baza ($n = 2$):** Graf sa 2 čvora i 0 grana nije povezan.

**Induktivna hipoteza:** Pretpostavimo da graf sa $n$ čvorova i manje od $n-1$ grana nije povezan.

**Induktivni korak:** Neka je $G$ graf sa $n+1$ čvorova i manje od $n$ grana. Dokazaćemo da on nije povezan.

Na osnovu činjenice da u grafu imamo manje grana nego čvorova, postoji čvor $v$ čiji je stepen $\deg_G(v) \leq 1$.

**Slučaj 1:** Ako je $\deg_G(v) = 0$, onda je on izolovan, nije povezan ni sa jednim drugim čvorom i čini svoju komponentu povezanosti. Broj komponenti je bar 2, te graf nije povezan.

**Slučaj 2:** Ako je $\deg_G(v) = 1$, onda graf $G$ ima jednak broj komponenti povezanosti kao i graf $G' = G - v$. Graf $G' = (V \setminus \{v\}, E \setminus \{\{u,v\}\})$ za neki čvor $u \in V$ je graf sa $n$ čvorova i manje od $n-1$ grana. Po induktivnoj hipotezi zaključujemo da $G'$ nije povezan, odnosno $\omega(G') > 1$. Kako je $\omega(G') = \omega(G) > 1$, sledi da ni graf $G$ nije povezan.

### 5.3 Primer grafa koji ilustruje teoremu

Za $n = 5$, minimalan broj grana za povezanost je $n-1 = 4$.

**Primer grafa sa 5 čvorova i 4 grane koji je povezan:**
```
Graf: G₁ = ({1,2,3,4,5}, {{1,2}, {2,3}, {3,4}, {4,5}})
Struktura: 1-2-3-4-5 (put)
Povezanost: ✓ Povezan
```

**Primer grafa sa 5 čvorova i 3 grane koji nije povezan:**
```
Graf: G₂ = ({1,2,3,4,5}, {{1,2}, {3,4}, {4,5}})
Struktura: 1-2    3-4-5
Komponente: {1,2}, {3,4,5}
Povezanost: ✗ Nije povezan, ω(G₂) = 2
```

## 6. Primer grafa sa n čvorova i bar n-1 grana koji nije povezan

### 6.1 Konstrukcija primera

Za $n = 6$, konstruišimo graf sa 6 čvorova i tačno 5 grana koji nije povezan:

**Graf:** $G = (\{1,2,3,4,5,6\}, \{\{1,2\}, \{1,3\}, \{2,3\}, \{4,5\}, \{5,6\}\})$

**Struktura:**
```
Komponenta 1: Trougao
   1
  / \
 2---3

Komponenta 2: Put
4---5---6
```

**Analiza:**
- Broj čvorova: $n = 6$
- Broj grana: $5 = n-1$ (minimalan potreban broj)
- Broj komponenti: $\omega(G) = 2$
- Povezanost: Graf nije povezan

Ovaj primer pokazuje da samo postojanje $n-1$ grana nije dovoljno za povezanost - važna je i njihova distribucija.

### 6.2 Opšti princip

Za bilo koji $n \geq 4$, možemo konstruisati nepovezan graf sa $n$ čvorova i $n-1$ grana tako što:
1. Formiramo kompletni graf $K_3$ sa prva 3 čvora (3 grane)
2. Formiramo put sa preostalih $n-3$ čvorova ($n-4$ grane)
3. Ukupno: $3 + (n-4) = n-1$ grana, ali graf ima 2 komponente

## 7. Teorema o uklanjanju grane konture

### 7.1 Formulacija teoreme

**Teorema:** Neka je $G = (V, E)$ povezan i neka je $C$ kontura u grafu $G$. Ako je $e$ grana konture, onda je $G - e$ i dalje povezan.

### 7.2 Dokaz

**Dokaz:** Izaberemo bilo koja dva čvora $u, v \in V$. Kako je $G$ povezan, postoji $uv$-put:

$$P = u v_1 v_2 \ldots v_i v_{i+1} \ldots v_{n-1} v$$

Razlikujemo dva slučaja:

**Slučaj 1:** Grana $e$ ne pripada $uv$-putu $P$. Onda je $P$ i $uv$-put u grafu $G - e$.

**Slučaj 2:** Grana $e$ pripada putu $P$. Pretpostavimo da je to grana $\{v_i, v_{i+1}\}$ i da je kontura $C$ oblika:
$$C: v_i v_{i+1} u_1 u_2 \ldots u_l v_i$$

To znači da u grafu $G - e$ postoji $v_i v_{i+1}$-put $Q$ oblika:
$$Q: v_i u_l u_{l-1} \ldots u_2 u_1 v_{i+1}$$
(u suprotnom smeru konture $C$)

Onda je:
$$S = u v_1 v_2 \ldots v_{i-1} v_i Q v_{i+1} v_{i+2} \ldots v_{n-1} v$$
šetnja u grafu $G - e$ od $u$ do $v$.

Na osnovu teoreme da ukoliko postoji $uv$-šetnja u grafu, onda postoji $uv$-put u istom grafu, zaključujemo da i u grafu $G - e$ postoji $uv$-put.

Kako između svaka dva čvora $u, v \in V$ postoji put u grafu $G - e$, sledi da je $G - e$ povezan.

### 7.3 Intuitivno objašnjenje

Ova teorema je intuitivno jasna: kontura predstavlja "redundantnu" vezu u smislu povezanosti. Svaka grana konture se može "zaobići" putem preostalih grana konture, pa uklanjanje jedne grane konture ne narušava povezanost grafa.

## 8. Dodatni pojmovi povezanosti

### 8.1 Razdelni čvorovi i mostovi

**Definicija:** Neka je $G = (V, E, \Psi)$ multigraf sa osobinom $\omega(G) = k \geq 1$.

- **Čvor $v \in V$ je razdelni (artikulacioni)** ako je $\omega(G - v) > k$
- **Grana $e \in E$ je razdelna (most)** ako je $\omega(G - e) > k$

### 8.2 Rastojanje između čvorova

**Definicija:** Neka je $G = (V, E)$ povezan graf. **Rastojanje $d(u,v)$** između različitih čvorova $u$ i $v$ jeste dužina najkraćeg puta od $u$ do $v$. Po definiciji uzimamo da je $d(u,u) = 0$.

**Svojstva rastojanja:** Funkcija $d: V^2 \to \mathbb{N}_0$ je metrika i važe sledeće osobine:

1. $d(u,v) \geq 0$
2. $d(u,v) = 0 \Leftrightarrow u = v$
3. $d(u,v) = d(v,u)$ (simetričnost)
4. $d(u,v) + d(v,w) \geq d(u,w)$ (nejednakost trougla)

## 9. Implementacija i algoritmi

### 9.1 Algoritam za transformaciju šetnje u put

```python
def transform_walk_to_path(self, walk):
    path = []
    last_occurrence = {}  # Track last seen index of each vertex
    
    for vertex in walk:
        if vertex in last_occurrence:
            # Remove cycles by keeping only up to the last occurrence
            path = path[:last_occurrence[vertex]]
        
        # Update last occurrence and add vertex to path
        last_occurrence[vertex] = len(path)
        path.append(vertex)

    return path
```

### 9.2 Algoritam za proveru povezanosti (DFS)

```python
def is_connected(self):
    if not self.graph:
        return False

    visited = set()
    # Start DFS from an arbitrary node
    self.dfs(next(iter(self.graph)), visited)
    
    # If all nodes are visited, the graph is connected
    return len(visited) == len(self.graph)
```

### 9.3 Algoritam za pronalaženje puta

```python
def find_path(self, start, end):
    visited = set()
    path = []

    def dfs(v):
        if v == end:
            path.append(v)
            return True
        visited.add(v)
        for neighbor in self.graph[v]:
            if neighbor not in visited:
                if dfs(neighbor):
                    path.append(v)
                    return True
        return False
    
    dfs(start)
    return path[::-1] if path else None
```

## 10. Praktične primene

### 10.1 Transportne mreže

U modelovanju putnih mreža, povezanost grafa određuje da li je moguće doći od bilo koje tačke do bilo koje druge tačke u mreži. Mostovi predstavljaju kritične veze čije uklanjanje može izolovati delove mreže.

### 10.2 Komunikacione mreže

U računarskim mrežama, povezanost grafa osigurava da svaki čvor može komunicirati sa svim ostalim čvorovima. Razdelni čvorovi predstavljaju kritične servere čiji kvar može narušiti komunikaciju.

### 10.3 Društvene mreže

U analizi društvenih mreža, povezanost pomaže u razumevanju kako se informacije prenose kroz mrežu i koje su ključne veze za održavanje komunikacije.

## Zaključak

Povezanost grafova je fundamentalni koncept koji omogućava dublje razumevanje strukture grafova i njihovih svojstava. Kroz sistematično proučavanje šetnji, staza, puteva i kontura, kao i relacije povezanosti kao ekvivalentne relacije, dolazimo do moćnih teorijskih rezultata koji imaju široku praktičnu primenu.

Ključne teoreme o minimalnom broju grana potrebnom za povezanost i o uticaju uklanjanja grana konture pružaju važne uvide u strukturu povezanih grafova i omogućavaju optimizaciju različitih mrežnih sistema.

Implementacija algoritama za rad sa povezanošću grafova omogućava praktičnu primenu teorijskih rezultata u rešavanju realnih problema u različitim oblastima kao što su transport, komunikacije i analiza društvenih mreža.