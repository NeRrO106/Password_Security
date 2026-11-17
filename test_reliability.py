
from password_stats.reliability import (
    effective_entropy,
    mttf_seconds,
    survival_probability,
    humanize_seconds,
)


def main():
    length = 12
    entropy_per_character = 6.0
    rate = 1_000_000_000  # Ipoteza: un miliard de incercari pe secunda

    total_entropy = effective_entropy(
        entropy_per_character,
        entropy_per_character,
        length,
    )

    mttf = mttf_seconds(total_entropy, rate)

    print(f"Entropie estimata: {total_entropy:.2f} biti")
    print(f"Rata presupusa: {rate:,} incercari/secunda")
    print(f"MTTF: {humanize_seconds(mttf)}")
    print(f"R(t) dupa o zi: {survival_probability(86400, mttf):.8f}")


if __name__ == "__main__":
    main()
