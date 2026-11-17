from password_stats.generators import (
    N,
    gen_secure,
    gen_mt,
    to_indices,
)
from password_stats.randomness_tests import (
    chi2_uniform,
    interpret_p_value,
)


def main():
    n = 1000
    length = 12

    datasets = {
        "secrets": gen_secure(n, length),
        "random.Random": gen_mt(n, length, seed=42),
    }

    for name, passwords in datasets.items():
        indices = to_indices(passwords)
        result = chi2_uniform(indices, N)

        print(f"\nGenerator: {name}")
        print(f"Statistica chi-patrat: {result['chi2']:.4f}")
        print(f"Grade de libertate: {result['degrees_of_freedom']}")
        print(f"p-value: {result['p_value']:.6f}")
        print(interpret_p_value(result["p_value"], alpha=0.05))


if __name__ == "__main__":
    main()