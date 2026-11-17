
from password_stats.generators import (
    ALPHABET,
    N,
    gen_secure,
    gen_mt,
    to_indices,
)
from password_stats.entropy import (
    shannon_entropy,
    miller_madow_entropy,
    bootstrap_entropy,
    theoretical_entropy,
)
from password_stats.randomness_tests import chi2_uniform
from password_stats.bigram import analyze_bigram


NUMBER = 1000
LENGTH = 12
CONFIDENCE = 0.95
SEED = 42


def analyze_generator(name, passwords):
    print(f"\n{'=' * 60}")
    print(f"Generator: {name}")
    print(f"Numar parole: {len(passwords)}")
    print(f"Lungime parola: {len(passwords[0])}")

    # Analiza simbolurilor pe toate pozitiile
    symbols = list("".join(passwords))

    entropy = shannon_entropy(symbols)
    corrected_entropy = miller_madow_entropy(symbols)
    interval = bootstrap_entropy(
        symbols,
        repetitions=1000,
        confidence=CONFIDENCE,
        seed=SEED,
    )

    print("\n[Entropie]")
    print(f"Entropie teoretica per simbol: {theoretical_entropy(N):.4f} biti")
    print(f"Entropie Shannon estimata:     {entropy:.4f} biti")
    print(f"Corectie Miller-Madow:         {corrected_entropy:.4f} biti")
    print(
        f"Interval bootstrap 95%:        "
        f"[{interval[0]:.4f}, {interval[1]:.4f}]"
    )

    # Test chi-patrat pe frecventele simbolurilor
    indices = to_indices(passwords)
    flat_indices = indices.flatten()
    chi2, p_value, df = chi2_uniform(
        flat_indices,
        alphabet_size=N,
    )

    print("\n[Test chi-patrat]")
    print(f"Statistica: {chi2:.4f}")
    print(f"Grade de libertate: {df}")
    print(f"p-value: {p_value:.6f}")
    if p_value < 0.05:
        print("Respingem H0 la nivelul alpha = 0.05.")
    else:
        print("Nu respingem H0 la nivelul alpha = 0.05.")

    # Analiza dependentelor dintre caractere consecutive
    marginal, conditional, mutual_info, redundancy = analyze_bigram(
        indices,
        alphabet_size=N,
    )

    print("\n[Analiza bigramelor]")
    print(f"Entropie marginala:  {marginal:.4f} biti")
    print(f"Entropie conditionata: {conditional:.4f} biti")
    print(f"Informatii mutuale:   {mutual_info:.4f} biti")
    print(f"Redundanta:           {redundancy:.4f}%")


def main():
    print("ANALIZA STATISTICA A GENERATOARELOR DE PAROLE")
    print(f"Alfabet: {N} simboluri")
    print(f"Entropie teoretica per simbol: {theoretical_entropy(N):.4f} biti")
    print(f"Numar parole per generator: {NUMBER}")
    print(f"Lungime parole: {LENGTH}")

    secure_passwords = gen_secure(NUMBER, LENGTH)
    mt_passwords = gen_mt(NUMBER, LENGTH, seed=SEED)

    analyze_generator("secrets", secure_passwords)
    analyze_generator("random.Random", mt_passwords)

    print("\n\nNota: trecerea testelor statistice nu demonstreaza securitate criptografica.")
    print("random.Random nu este recomandat pentru generarea parolelor reale.")


if __name__ == "__main__":
    main()
