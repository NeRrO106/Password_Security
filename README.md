```
```
# Analizor Statistic de Complexitate a Parolei

Acesta este un script Python interactiv care evaluează securitatea unei parole folosind metrici statistice și matematice, cum ar fi **Entropia Shannon** și **Entropia Teoretică**, pe lângă analiza structurală clasică (lungime, diversitate de caractere și pattern-uri comune).

---

## 🚀 Caracteristici

* **Calculul Entropiei Shannon:** Măsoară gradul de impredictibilitate și distribuția caracterelor în interiorul parolei introduse.
* **Calculul Entropiei Teoretice:** Determină spațiul total de căutare pe baza dimensiunii alfabetului ($N^L$) transpus în biți de securitate ($L \cdot \log_2 N$).
* **Analiză Structurală:** Verifică prezența literelor mari, literelor mici, cifrelor și a simbolurilor speciale.
* **Sistem de Penalizare:** Detectează secvențe comune sau periculoase (ex: `123456`, `password`, `qwerty`) și utilizarea excesivă a caracterelor repetitive.
* **Sistem de Scoring și Verdict:** Generează un scor final de la 0 la 100 și încadrează parola într-o categorie de siguranță (de la *Foarte slabă* la *Foarte puternică*).
* **Recomandări Inteligente:** Oferă sfaturi personalizate pentru îmbunătățirea securității în funcție de punctele slabe identificate.

---

## 📊 Concepte Matematice Utilizate

### 1. Entropia Shannon
Măsoară incertitudinea conținută în textul parolei. Formula aplicată pentru fiecare caracter cu probabilitatea $p_i$ este:

$$H = -\sum_{i=1}^{n} p_i \log_2 p_i$$

### 2. Entropia Teoretică (Biți de Securitate)
Reprezintă numărul de biți necesari pentru a sparge parola prin brute-force, considerând că atacatorul cunoaște setul de caractere folosit. Formula este:

$$E = L \cdot \log_2 N$$

Unde:
* $L$ = lungimea parolei.
* $N$ = dimensiunea totală a alfabetului potențial (Litere mici: 26, Litere mari: 26, Cifre: 10, Simboluri: 32).

---

## 🛠️ Cerințe și Instalare

Scriptul folosește doar librăriile native din Python (`math`, `string`, `collections`), ceea ce înseamnă că **nu este necesară instalarea unor pachete externe**.

1. Asigură-te că ai instalat **Python 3.6+**.
2. Clonează sau descarcă acest repository.
3. Salvează codul într-un fișier numit `analizor_parole.py`.

---

## 💻 Utilizare

Rulează scriptul din terminal folosind comanda:

```bash
python analizor_parole.py
```
### Exemplu de rulare în consolă:

```text
=======================================================
   ANALIZATOR STATISTIC DE COMPLEXITATE A PAROLEI
=======================================================

Introdu parola pentru analiză: P@ss1234!

=======================================================
                REZULTATE ANALIZĂ
=======================================================
Parolă analizată: P@ss1234!
Lungime: 9 caractere

--- Tipuri de caractere ---
Litere mici: DA
Litere mari: DA
Cifre: DA
Simboluri: DA

--- Entropie ---
Entropie Shannon: 2.95 biți/simbol
Entropie totală: 26.53 biți
Entropie teoretică: 59.26 biți

--- Evaluare securitate ---
Scor final: 65/100
Verdict: Medie

--- Recomandări ---
- Folosește o parolă mai lungă.

```

---

## 📐 Logica de Scoring

Scorul final (0-100) este determinat pe baza următoarelor criterii:

* **Lungime:** Până la +25 puncte (pentru lungimi $\ge$ 12 caractere).
* **Diversitate:** +10 puncte pentru fiecare tip de caracter unic detectat (Litere mari/mici/cifre/simboluri) -> Maxim +40 puncte.
* **Entropie Teoretică:** Până la +35 puncte (dacă entropia $\ge$ 60 biți).
* **Penalizări:** * `-20 puncte` pentru includerea de pattern-uri comune (`admin`, `123456`, etc.).
* `-15 puncte` dacă parola este formată din doar 1 sau 2 caractere unice repetitive.



### Praguri pentru Verdict:

* **< 30:** Foarte slabă
* **30 - 49:** Slabă
* **50 - 69:** Medie
* **70 - 89:** Puternică
* **90 - 100:** Foarte puternică
