
import math


def effective_entropy(marginal_entropy, conditional_entropy, length):
    if length < 1:
        raise ValueError("Lungimea trebuie sa fie pozitiva.")

    if marginal_entropy < 0 or conditional_entropy < 0:
        raise ValueError("Entropiile nu pot fi negative.")

    return marginal_entropy + (length - 1) * conditional_entropy


def mttf_seconds(entropy_bits, guesses_per_second):
    if entropy_bits < 0:
        raise ValueError("Entropia nu poate fi negativa.")

    if guesses_per_second <= 0:
        raise ValueError("Rata de incercari trebuie sa fie pozitiva.")

    return (2.0 ** entropy_bits) / guesses_per_second


def survival_probability(time_seconds, mttf):
    """Model exponential simplificat R(t) = exp(-t / MTTF)."""
    if mttf <= 0:
        raise ValueError("MTTF trebuie sa fie pozitiv.")

    if time_seconds < 0:
        raise ValueError("Timpul nu poate fi negativ.")

    return math.exp(-time_seconds / mttf)


def humanize_seconds(seconds):
    units = [
        ("ani", 365.25 * 24 * 3600),
        ("zile", 24 * 3600),
        ("ore", 3600),
        ("minute", 60),
        ("secunde", 1),
    ]

    for name, factor in units:
        if seconds >= factor:
            return f"{seconds / factor:.2f} {name}"

    return f"{seconds * 1000:.2f} milisecunde"
