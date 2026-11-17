
import math
import numpy as np

from password_stats.entropy import shannon_entropy


def conditional_entropy(indices, alphabet_size=64):
    indices = np.asarray(indices, dtype=np.int64)

    if indices.ndim != 2 or indices.shape[1] < 2:
        raise ValueError("Sunt necesare parole cu cel putin 2 caractere.")

    if np.any(indices < 0) or np.any(indices >= alphabet_size):
        raise ValueError("Indici in afara alfabetului.")

    previous = indices[:, :-1].ravel()
    current = indices[:, 1:].ravel()

    pair_counts = np.bincount(
        previous * alphabet_size + current,
        minlength=alphabet_size ** 2,
    ).reshape(alphabet_size, alphabet_size)

    total = pair_counts.sum()
    row_totals = pair_counts.sum(axis=1)

    entropy = 0.0

    for i in range(alphabet_size):
        if row_totals[i] == 0:
            continue

        probabilities = pair_counts[i] / row_totals[i]
        probabilities = probabilities[probabilities > 0]

        conditional = -np.sum(
            probabilities * np.log2(probabilities)
        )

        entropy += (row_totals[i] / total) * conditional

    return float(entropy)


def analyze_bigram(indices, alphabet_size=64):
    indices = np.asarray(indices, dtype=np.int64)

    if indices.ndim != 2 or indices.shape[1] < 2:
        raise ValueError("Matricea trebuie sa contina parole de lungime >= 2.")

    marginal_entropy = shannon_entropy(indices[:, 1:].ravel())
    conditional = conditional_entropy(indices, alphabet_size)

    mutual_information = max(0.0, marginal_entropy - conditional)
    redundancy = 1.0 - marginal_entropy / math.log2(alphabet_size)

    return {
        "marginal_entropy": marginal_entropy,
        "conditional_entropy": conditional,
        "mutual_information": mutual_information,
        "redundancy": redundancy,
    }
