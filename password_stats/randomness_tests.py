
import math
from scipy.special import erfc
import numpy as np


def to_bits(indices, alphabet_size=64):
    if alphabet_size < 2 or alphabet_size & (alphabet_size - 1):
        raise ValueError("Alfabetul trebuie sa aiba dimensiune putere a lui 2.")

    indices = np.asarray(indices, dtype=np.int64)

    if indices.size == 0:
        raise ValueError("Datele nu pot fi goale.")

    if np.any(indices < 0) or np.any(indices >= alphabet_size):
        raise ValueError("Indici in afara alfabetului.")

    bits_per_symbol = int(math.log2(alphabet_size))
    shifts = np.arange(bits_per_symbol - 1, -1, -1)

    return ((indices[..., None] >> shifts) & 1).astype(np.int8).ravel()


def monobit_test(bits):
    bits = np.asarray(bits, dtype=np.int8).ravel()

    if bits.size == 0 or not np.isin(bits, [0, 1]).all():
        raise ValueError("Sunt necesari biti 0/1, iar secventa nu poate fi goala.")

    n = bits.size
    s = int(np.sum(2 * bits - 1))
    statistic = abs(s) / math.sqrt(n)
    p_value = erfc(statistic / math.sqrt(2))

    return {
        "statistic": float(statistic),
        "p_value": float(p_value),
        "n_bits": int(n),
    }


def runs_test(bits):
    bits = np.asarray(bits, dtype=np.int8).ravel()

    if bits.size < 2 or not np.isin(bits, [0, 1]).all():
        raise ValueError("Sunt necesari cel putin doi biti, 0 sau 1.")

    n = bits.size
    proportion = float(bits.mean())

    if abs(proportion - 0.5) >= 2 / math.sqrt(n):
        return {
            "runs": int(1 + np.count_nonzero(bits[1:] != bits[:-1])),
            "p_value": 0.0,
            "applicable": False,
            "reason": "Proportia de biti 1 nu indeplineste prerechizitul.",
        }

    runs = int(1 + np.count_nonzero(bits[1:] != bits[:-1]))
    numerator = abs(runs - 2 * n * proportion * (1 - proportion))
    denominator = 2 * math.sqrt(2 * n) * proportion * (1 - proportion)
    p_value = erfc(numerator / denominator)

    return {
        "runs": runs,
        "p_value": float(p_value),
        "applicable": True,
        "reason": "",
    }


def interpret_p_value(p_value, alpha=0.05):
    if not 0 < alpha < 1:
        raise ValueError("alpha trebuie sa fie intre 0 si 1.")

    if p_value < alpha:
        return "Respingem H0 la nivelul de semnificatie ales."

    return "Nu respingem H0 la nivelul de semnificatie ales."


