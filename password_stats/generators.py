import random
import secrets
import string
import numpy as np


ALPHABET = string.ascii_letters + string.digits + "!@"
N = len(ALPHABET)

_LOOKUP = {char: index for index, char in enumerate(ALPHABET)}


def _validate_parameters(number, length):
    if number < 1:
        raise ValueError("Numarul de parole trebuie sa fie pozitiv.")
    if length < 1:
        raise ValueError("Lungimea parolei trebuie sa fie pozitiva.")


def gen_secure(number, length):
    _validate_parameters(number, length)

    return [
        "".join(secrets.choice(ALPHABET) for _ in range(length))
        for _ in range(number)
    ]


def gen_mt(number, length, seed=0):
    _validate_parameters(number, length)

    rng = random.Random(seed)

    return [
        "".join(rng.choices(ALPHABET, k=length))
        for _ in range(number)
    ]


def to_indices(passwords):
    passwords = list(passwords)

    if not passwords:
        return np.empty((0, 0), dtype=np.int64)

    length = len(passwords[0])

    if any(len(password) != length for password in passwords):
        raise ValueError("Toate parolele trebuie sa aiba aceeasi lungime.")

    invalid = set("".join(passwords)) - set(ALPHABET)

    if invalid:
        raise ValueError(
            f"Caractere care nu apartin alfabetului: {sorted(invalid)}"
        )

    return np.array(
        [[_LOOKUP[char] for char in password] for password in passwords],
        dtype=np.int64,
    )


def main():
    number = 5
    length = 8

    secure_passwords = gen_secure(number, length)
    mt_passwords = gen_mt(number, length, seed=42)

    print(f"Alfabet: {ALPHABET}")
    print(f"Numar simboluri: {N}")
    print(f"Entropie teoretica per simbol: {np.log2(N):.1f} biti")

    print("\nExemple secrets:")
    for password in secure_passwords:
        print(password)

    print("\nExemple random.Random:")
    for password in mt_passwords:
        print(password)

    indices = to_indices(mt_passwords)

    print("\nMatricea de indici:")
    print(indices)
    print("Dimensiunea matricei:", indices.shape)


if __name__ == "__main__":
    main()
