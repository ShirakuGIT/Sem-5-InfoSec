"""
1. Encrypt the message "I am learning information security" using one of
the following ciphers. Ignore the space between words. Decrypt the
message to get the original plaintext:
    a) Additive cipher with key = 20
    b) Multiplicative cipher with key = 15
    c) Affine cipher with key = (15, 20)
"""

message = "Iamlearninginformationsecurity".replace(" ", "").upper()

# Alphabet size
alphabet_size = 26

def additive_cipher_encrypt(message, key):
    return ''.join([chr(((ord(char) - ord('A') + key) % alphabet_size) + ord('A')) for char in message])

def additive_cipher_decrypt(ciphertext, key):
    return ''.join([chr(((ord(char) - ord('A') - key) % alphabet_size) + ord('A')) for char in ciphertext])

key = 20
ciphertext = additive_cipher_encrypt(message, key)
decrypted_message = additive_cipher_decrypt(ciphertext, key)

print(f"Additive Cipher Ciphertext: {ciphertext}")
print(f"Decrypted Message: {decrypted_message}")


def multiplicative_cipher_encrypt(message, key):
    return ''.join([chr(((ord(char) - ord('A')) * key % alphabet_size) + ord('A')) for char in message])

def multiplicative_cipher_decrypt(ciphertext, key):
    # Find the modular inverse of the key
    def mod_inverse(a, m):
        for i in range(1, m):
            if (a * i) % m == 1:
                return i
        return -1
    
    inv_key = mod_inverse(key, alphabet_size)
    return ''.join([chr(((ord(char) - ord('A')) * inv_key % alphabet_size) + ord('A')) for char in ciphertext])

key = 15
ciphertext = multiplicative_cipher_encrypt(message, key)
decrypted_message = multiplicative_cipher_decrypt(ciphertext, key)

print(f"Multiplicative Cipher Ciphertext: {ciphertext}")
print(f"Decrypted Message: {decrypted_message}")

def affine_cipher_encrypt(message, mult_key, add_key):
    return ''.join([chr((((ord(char) - ord('A')) * mult_key + add_key) % alphabet_size) + ord('A')) for char in message])

def affine_cipher_decrypt(ciphertext, mult_key, add_key):
    # Find the modular inverse of the multiplicative key
    def mod_inverse(a, m):
        for i in range(1, m):
            if (a * i) % m == 1:
                return i
        return -1

    inv_key = mod_inverse(mult_key, alphabet_size)
    return ''.join([chr(((inv_key * (ord(char) - ord('A') - add_key)) % alphabet_size) + ord('A')) for char in ciphertext])

mult_key, add_key = 15, 20
ciphertext = affine_cipher_encrypt(message, mult_key, add_key)
decrypted_message = affine_cipher_decrypt(ciphertext, mult_key, add_key)

print(f"Affine Cipher Ciphertext: {ciphertext}")
print(f"Decrypted Message: {decrypted_message}")

