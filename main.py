from big_int import BigInt
from rsa_encryption import *

def make_rsa_keys():
    big_int = BigInt()
    print("Mathematical operations testing:")
    print(big_int.calculate("sum 34567324987890 3456789087654"))
    print(big_int.calculate("mul 34567324987890 3456789087654"))
    print(big_int.calculate("sqr 15687245292409"))
    print(big_int.calculate("mod 345678904568456 100579"))

    keys = generate_keys(12)
    initial_text = "Laba na max baliv"
    encrypted_text = rsa_encrypt(keys[0], initial_text)
    decrypted_text = rsa_decrypt(keys[1], encrypted_text)
    print("Ключі - ", keys)
    print("Початковий текст - ", initial_text)
    print("Зашифрований текст - ", encrypted_text)
    print("Розшифрований текст - ", decrypted_text)


if __name__ == '__main__':
    make_rsa_keys()
