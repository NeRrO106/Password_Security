
from password_stats.generators import gen_secure, gen_mt, to_indices, N
from password_stats.bigram import analyze_bigram


def main():
    datasets = {
        "secrets": gen_secure(5000, 12),
        "random.Random": gen_mt(5000, 12, seed=42),
    }

    for name, passwords in datasets.items():
        result = analyze_bigram(to_indices(passwords), N)

        print(f"\nGenerator: {name}")
        print(f"Entropie marginala: {result['marginal_entropy']:.4f} biti")
        print(f"Entropie conditionata: {result['conditional_entropy']:.4f} biti")
        print(f"Informatii mutuale: {result['mutual_information']:.4f} biti")
        print(f"Redundanta: {result['redundancy']:.4%}")


if __name__ == "__main__":
    main()
