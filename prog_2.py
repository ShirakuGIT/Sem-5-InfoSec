"""
2. Encrypt the message "the house is being sold tonight" using one of the
following ciphers. Ignore the space between words. Decrypt the
message to get the original plaintext:
    • Vigenere cipher with key: "dollars"
    • Autokey cipher with key = 7
"""

message = "thehouseisbeingsoldtonight".replace(" ", "").upper()
alphabet_size = 26

def vigenere_cipher_encrypt(message, key):
    key = key.upper()
    key_repeat = (key * (len(message) // len(key) + 1))[:len(message)]
    return ''.join([chr(((ord(m) - ord('A') + ord(k) - ord('A')) % alphabet_size) + ord('A')) for m, k in zip(message, key_repeat)])

def vigenere_cipher_decrypt(ciphertext, key):
    key = key.upper()
    key_repeat = (key * (len(ciphertext) // len(key) + 1))[:len(ciphertext)]
    return ''.join([chr(((ord(c) - ord('A') - (ord(k) - ord('A'))) % alphabet_size) + ord('A')) for c, k in zip(ciphertext, key_repeat)])

key = "dollars"
ciphertext = vigenere_cipher_encrypt(message, key)
decrypted_message = vigenere_cipher_decrypt(ciphertext, key)

print(f"Vigenere Cipher Ciphertext: {ciphertext}")
print(f"Decrypted Message: {decrypted_message}")

def autokey_cipher_encrypt(message, key):
    key_stream = [key] + [ord(m) - ord('A') for m in message[:-1]]
    return ''.join([chr(((ord(m) - ord('A') + k) % alphabet_size) + ord('A')) for m, k in zip(message, key_stream)])

def autokey_cipher_decrypt(ciphertext, key):
    decrypted_message = ""
    current_key = key
    for c in ciphertext:
        decrypted_char = chr(((ord(c) - ord('A') - current_key) % alphabet_size) + ord('A'))
        decrypted_message += decrypted_char
        current_key = ord(decrypted_char) - ord('A')
    return decrypted_message

key = 7
ciphertext = autokey_cipher_encrypt(message, key)
decrypted_message = autokey_cipher_decrypt(ciphertext, key)

print(f"Autokey Cipher Ciphertext: {ciphertext}")
print(f"Decrypted Message: {decrypted_message}")
