
import secrets
import statistics
import matplotlib.pyplot as plt

from password_stats.entropy import (
    shannon_entropy,
    miller_madow_entropy,
    bootstrap_entropy,
    theoretical_entropy,
)


ALPHABET = "0123456789"
PASSWORD_LENGTH = 12
SAMPLE_SIZES = [10, 25, 50, 100, 250, 500, 1000]
TRIALS = 100


def generate_passwords(number, length):
    return [
        "".join(secrets.choice(ALPHABET) for _ in range(length))
        for _ in range(number)
    ]


def run_experiment():
    true_entropy = theoretical_entropy(len(ALPHABET))

    plugin_means = []
    corrected_means = []

    print("EXPERIMENT: ESTIMAREA ENTROPIEI")
    print(f"Alfabet: {ALPHABET}")
    print(f"Lungimea fiecarei parole: {PASSWORD_LENGTH}")
    print(f"Entropia teoretica: {true_entropy:.4f} biti/simbol")
    print(f"Experimente repetate pentru fiecare dimensiune: {TRIALS}")
    print("-" * 78)
    print(
        f"{'Nr. parole':>12} {'Plug-in mediu':>16} "
        f"{'Miller-Madow mediu':>21} {'Bias plug-in':>15}"
    )

    for number in SAMPLE_SIZES:
        plugin_values = []
        corrected_values = []

        for _ in range(TRIALS):
            passwords = generate_passwords(number, PASSWORD_LENGTH)
            symbols = "".join(passwords)

            plugin_values.append(shannon_entropy(symbols))
            corrected_values.append(miller_madow_entropy(symbols))

        plugin_mean = statistics.mean(plugin_values)
        corrected_mean = statistics.mean(corrected_values)
        bias = plugin_mean - true_entropy

        plugin_means.append(plugin_mean)
        corrected_means.append(corrected_mean)

        print(
            f"{number:>12} {plugin_mean:>16.4f} "
            f"{corrected_mean:>21.4f} {bias:>15.4f}"
        )

    final_passwords = generate_passwords(
        max(SAMPLE_SIZES), PASSWORD_LENGTH
    )
    final_symbols = "".join(final_passwords)

    lower, upper = bootstrap_entropy(
        final_symbols, repetitions=1000, confidence=0.95
    )

    print("\nInterval bootstrap 95% pentru ultimul esantion:")
    print(f"[{lower:.4f}, {upper:.4f}] biti/simbol")

    plt.figure(figsize=(10, 6))

    plt.plot(
        SAMPLE_SIZES, plugin_means,
        marker="o", label="Estimator plug-in"
    )
    plt.plot(
        SAMPLE_SIZES, corrected_means,
        marker="s", label="Miller-Madow"
    )
    plt.axhline(
        true_entropy, linestyle="--",
        label="Entropia teoretica"
    )

    plt.xscale("log")
    plt.xlabel("Numarul de parole")
    plt.ylabel("Entropie estimata (biti/simbol)")
    plt.title("Bias-ul estimarii entropiei in functie de esantion")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig("entropy_experiment_plot.png", dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    run_experiment()
