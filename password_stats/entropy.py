import math
import random
from collections import Counter

def shannon_entropy(symbols):
    symbols = list(symbols)

    if not symbols:
        return 0.0

    counts = Counter(symbols)
    n = len(symbols)

    return -sum(
        (count / n) * math.log2(count / n)
        for count in counts.values()
    )

def miller_madow_entropy(symbols):
    symbols = list(symbols)
    if not symbols:
        return 0.0

    n = len(symbols)
    k = len(set(symbols))

    return(
        shannon_entropy(symbols) + (k - 1) / (2 * n * math.log(2))
    )

def bootstrap_entropy(
        symbols, repetitions=1000, confidence=0.05, seed=42
    ):

    symbols = list(symbols)

    if not symbols:
        raise ValueError("Esantionul nu poate fi golit.")

    if repetitions < 100:
        raise ValueError("Foloseste cel putin 100 de repetitii.")

    if not 0 <  confidence < 1:
        raise ValueError("confidence trebuie sa fie intre 0 si 1.")

    rng = random.Random(seed)
    n = len(symbols)

    estimates = [
        shannon_entropy(rng.choices(symbols, k=n))
        for _ in range(repetitions)
    ]
    estimates.sort()

    tail = (1 - confidence) / 2
    lower = estimates[int(tail * repetitions)]
    upper = estimates[
        min(int((1-tail) * repetitions), repetitions - 1)
    ]
    return lower, upper

def theoretical_entropy(alphabet_size):
    if alphabet_size < 1:
        raise ValueError("Alfabetul trebuie sa aiba cel putin un simbol")

    return math.log2(alphabet_size)