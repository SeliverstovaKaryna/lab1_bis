from big_int import BigInt
from rsa_encryption import *
import time

def make_rsa_keys():
    big_int = BigInt()
    print("Mathematical operations testing:")
    print(big_int.calculate("sum 34567324987890 3456789087654"))
    print(big_int.calculate("mul 34567324987890 3456789087654"))
    print(big_int.calculate("sqr 15687245292409"))
    print(big_int.calculate("mod 345678904568456 100579"))

    print("Test with simple prime algorithm:")
    start = time.perf_counter()
    keys = generate_keys(12)
    end = time.perf_counter()
    print(f"Time taken: {end - start} seconds")
    print("____________________________________")
    print("Test with Ferma prime algorithm:")
    start2 = time.perf_counter()
    keys2 = generate_keys_ferma(12)
    end2 = time.perf_counter()
    print(f"Time taken: {end2 - start2} seconds")
    print("____________________________________")

    initial_text = "Laba nomer 2 na max baliv"

    print("RSA")
    encrypted_text = rsa_encrypt(keys[0], initial_text)
    decrypted_text = rsa_decrypt(keys[1], encrypted_text)
    print("Ключі - ", keys)
    print("Початковий текст - ", initial_text)
    print("Зашифрований текст - ", encrypted_text)
    print("Розшифрований текст - ", decrypted_text)

    print("____________________________________")
    print("RSA with Ferma prime algorithm:")
    encrypted_text2 = rsa_encrypt(keys[0], initial_text)
    decrypted_text2 = rsa_decrypt(keys[1], encrypted_text)
    print("Ключі - ", keys)
    print("Початковий текст - ", initial_text)
    print("Зашифрований текст - ", encrypted_text2)
    print("Розшифрований текст - ", decrypted_text2)



if __name__ == '__main__':
    make_rsa_keys()
