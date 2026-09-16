import random
from big_int import BigInt

def is_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True


def euler_func(p, q):
    bigInt = BigInt()
    return bigInt.calculate(f"mul {str((p - 1))} {str((q - 1))}")


def extended_euclidean_algorithm(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_euclidean_algorithm(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


def modular_inverse(num, mod):
    return extended_euclidean_algorithm(num, mod)[1] % mod


def generate_keys(bit_length):
    bigInt = BigInt()
    half_bit_length = bit_length // 2
    while True:
        p = random.randint(2 ** (half_bit_length - 1), 2 ** half_bit_length - 1)
        if is_prime(p):
            break
    while True:
        q = random.randint(2 ** (half_bit_length - 1), 2 ** half_bit_length - 1)
        if is_prime(q) and p != q:
            break

    n = int(bigInt.calculate(f"mul {str(p)} {str(q)}"))
    phi = int(euler_func(p, q))
    while True:
        e = random.randint(3, phi - 1)
        if extended_euclidean_algorithm(e, phi)[0] == 1:
            break
    pub_key = (e, n)
    d = modular_inverse(e, phi)
    priv_key = (d, n)
    return pub_key, priv_key


def rsa_encrypt(public_key, plain_text):
    e, n = public_key#ord is unicode code point
    return [pow(ord(char), e, n) for char in plain_text]


def rsa_decrypt(private_key, encrypted_text):
    d, n = private_key#chr is reverse to ord
    decrypted_text = [chr(pow(char, d, n)) for char in encrypted_text]
    return ''.join(decrypted_text)

