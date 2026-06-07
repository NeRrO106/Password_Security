import math
import string
from collections import Counter


def calculeaza_entropie_shannon(parola):
    frecvente = Counter(parola)
    lungime = len(parola)

    entropie = 0

    for caracter in frecvente:
        pi = frecvente[caracter] / lungime
        entropie -= pi * math.log2(pi)

    return entropie

def analiza_caractere(parola):
    are_litere_mici = any(c.islower() for c in parola)
    are_litere_mari = any(c.isupper() for c in parola)
    are_cifre = any(c.isdigit() for c in parola)
    are_simboluri = any(c in string.punctuation for c in parola)
    return {
        "litere_mici": are_litere_mici,
        "litere_mari": are_litere_mari,
        "cifre": are_cifre,
        "simboluri": are_simboluri
    }

def dimensiune_alfabet(analiza):
    N = 0

    if analiza["litere_mici"]:
        N += 26

    if analiza["litere_mari"]:
        N += 26

    if analiza["cifre"]:
        N += 10

    if analiza["simboluri"]:
        N += 32

    return N

def calculeaza_entropie_teoretica(parola, N):
    L = len(parola)

    if N == 0:
        return 0

    return L * math.log2(N)

def verifica_patternuri_slabe(parola):
    patternuri_slabe = [
        "123456",
        "password",
        "qwerty",
        "abcdef",
        "admin"
    ]

    parola_lower = parola.lower()

    penalizare = 0
    motive = []

    for pattern in patternuri_slabe:
        if pattern in parola_lower:
            penalizare += 20
            motive.append(f"Conține pattern slab: '{pattern}'")

    if len(set(parola)) <= 2:
        penalizare += 15
        motive.append("Prea multe caractere repetitive")

    return penalizare, motive

def calculeaza_scor(parola, entropia_teoretica, analiza):
    scor = 0

    lungime = len(parola)

    if lungime >= 12:
        scor += 25
    elif lungime >= 8:
        scor += 15
    else:
        scor += 5

    tipuri = sum(analiza.values())
    scor += tipuri * 10

    if entropia_teoretica >= 60:
        scor += 35
    elif entropia_teoretica >= 40:
        scor += 25
    elif entropia_teoretica >= 20:
        scor += 15
    else:
        scor += 5

    penalizare, motive = verifica_patternuri_slabe(parola)
    scor -= penalizare

    scor = max(0, min(100, scor))

    return scor, motive

def verdict_parola(scor):
    if scor < 30:
        return "Foarte slabă"
    elif scor < 50:
        return "Slabă"
    elif scor < 70:
        return "Medie"
    elif scor < 90:
        return "Puternică"
    else:
        return "Foarte puternică"

print("=" * 55)
print("   ANALIZATOR STATISTIC DE COMPLEXITATE A PAROLEI")
print("=" * 55)

parola = input("\nIntrodu parola pentru analiză: ")

entropie_shannon = calculeaza_entropie_shannon(parola)

entropie_totala = entropie_shannon * len(parola)

analiza = analiza_caractere(parola)

N = dimensiune_alfabet(analiza)

entropie_teoretica = calculeaza_entropie_teoretica(parola, N)

scor, motive = calculeaza_scor(
    parola,
    entropie_teoretica,
    analiza
)

verdict = verdict_parola(scor)

print("\n" + "=" * 55)
print("                REZULTATE ANALIZĂ")
print("=" * 55)

print(f"Parolă analizată: {parola}")
print(f"Lungime: {len(parola)} caractere")

print("\n--- Tipuri de caractere ---")
print(f"Litere mici: {'DA' if analiza['litere_mici'] else 'NU'}")
print(f"Litere mari: {'DA' if analiza['litere_mari'] else 'NU'}")
print(f"Cifre: {'DA' if analiza['cifre'] else 'NU'}")
print(f"Simboluri: {'DA' if analiza['simboluri'] else 'NU'}")

print("\n--- Entropie ---")
print(f"Entropie Shannon: {entropie_shannon:.2f} biți/simbol")
print(f"Entropie totală: {entropie_totala:.2f} biți")
print(f"Entropie teoretică: {entropie_teoretica:.2f} biți")

print("\n--- Evaluare securitate ---")
print(f"Scor final: {scor}/100")
print(f"Verdict: {verdict}")

if motive:
    print("\n--- Probleme detectate ---")
    for motiv in motive:
        print(f"- {motiv}")

print("\n--- Recomandări ---")

if len(parola) < 12:
    print("- Folosește o parolă mai lungă.")

if not analiza["litere_mari"]:
    print("- Adaugă litere mari.")

if not analiza["cifre"]:
    print("- Adaugă cifre.")

if not analiza["simboluri"]:
    print("- Adaugă simboluri speciale.")

if verdict in ["Foarte slabă", "Slabă"]:
    print("- Evită parolele comune și repetitive.")

print("\nAnaliza s-a încheiat.")