
from password_stats.generators import gen_secure, gen_mt, to_indices, N
from password_stats.randomness_tests import (
    to_bits,
    monobit_test,
    runs_test,
    interpret_p_value,
)


def main():
    datasets = {
        "secrets": gen_secure(1000, 12),
        "random.Random": gen_mt(1000, 12, seed=42),
    }

    for name, passwords in datasets.items():
        indices = to_indices(passwords)
        bits = to_bits(indices, N)

        mono = monobit_test(bits)
        runs = runs_test(bits)

        print(f"\nGenerator: {name}")
        print(
            f"Monobit: p-value={mono['p_value']:.6f}; "
            f"{interpret_p_value(mono['p_value'])}"
        )
        print(f"Runs observate: {runs['runs']}")
        print(f"Runs aplicabil: {runs['applicable']}")

        if runs["applicable"]:
            print(
                f"Runs: p-value={runs['p_value']:.6f}; "
                f"{interpret_p_value(runs['p_value'])}"
            )
        else:
            print("Runs nu se interpreteaza: prerechizitul nu este indeplinit.")


if __name__ == "__main__":
    main()
