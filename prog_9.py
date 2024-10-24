"""
Encrypt the message "Cryptographic Protocols" using the RSA public
key (n, e) where n = 323 and e = 5. Decrypt the ciphertext with the
private key (n, d) where d = 173 to confirm the original message
"""
"""
# Given RSA values
n = 323
e = 5
d = 173

# Message to encrypt
message = "Cryptographic Protocols"
message_int = [ord(c) for c in message]  # Convert message to integers

# Encrypt the message using RSA public key
ciphertext = [(m ** e) % n for m in message_int]

# Decrypt the message using RSA private key
decrypted_message = ''.join([chr((c ** d) % n) for c in ciphertext])

print(f"Original message: {message}")
print(f"Decrypted message: {decrypted_message}")

# Alternative Implementation
"""

"""

from Crypto.PublicKey import RSA
from Crypto.Util.number import bytes_to_long, long_to_bytes

# Given RSA values
n = 323
e = 5
d = 173

# Construct RSA key (public and private)
public_key = RSA.construct((n, e))
private_key = RSA.construct((n, d))

# Message to encrypt
message = "Cryptographic Protocols".encode()
message_int = bytes_to_long(message)

# Encrypt the message using RSA public key
ciphertext = pow(message_int, public_key.e, public_key.n)

# Decrypt the message using RSA private key
decrypted_message_int = pow(ciphertext, private_key.d, private_key.n)
decrypted_message = long_to_bytes(decrypted_message_int)

print(f"Ciphertext: {ciphertext}")
print(f"Decrypted message: {decrypted_message.decode()}")

"""

import rsa

# Given RSA key parameters
n = 323
e = 5
d = 173
p = 17
q = 19

# Construct public and private keys
public_key = rsa.PublicKey(n, e)
private_key = rsa.PrivateKey(n, e, d, p, q)


# Message to encrypt
message = "Cryptographic Protocols"

# Encrypt each character individually
ciphertext = []
for char in message:
    m = ord(char)  # Convert character to integer (ASCII value)
    if m >= n:
        raise ValueError(f"Character '{char}' (ASCII {m}) is too large to encrypt with n={n}.")
    c = pow(m, e, n)  # Encrypt: c = m^e mod n
    ciphertext.append(c)

print(f"Encrypted: {ciphertext}")

# Decrypt each character individually
decrypted_message = ''.join([chr(pow(c, d, n)) for c in ciphertext])

print(f"Decrypted: {decrypted_message}")


"""
# Manual RSA Encryption and Decryption for Educational Purposes

# Given RSA key parameters
n = 323
e = 5
d = 173

# Message to encrypt
message = "Cryptographic Protocols"

# Function to encrypt a single character
def rsa_encrypt_char(char, e, n):
    m = ord(char)  # Convert character to integer (ASCII value)
    if m >= n:
        raise ValueError(f"Character '{char}' (ASCII {m}) is too large to encrypt with n={n}.")
    c = pow(m, e, n)  # Encrypt: c = m^e mod n
    return c

# Function to decrypt a single integer back to character
def rsa_decrypt_char(c, d, n):
    m = pow(c, d, n)  # Decrypt: m = c^d mod n
    return chr(m)

# Encrypt the message character by character
ciphertext = []
for char in message:
    try:
        encrypted_char = rsa_encrypt_char(char, e, n)
        ciphertext.append(encrypted_char)
    except ValueError as ve:
        print(ve)
        # Handle characters that cannot be encrypted with the given n
        # For simplicity, we'll skip them
        continue

print(f"Encrypted Ciphertext (as integers): {ciphertext}")

# Decrypt the ciphertext back to the original message
decrypted_message = ''.join([rsa_decrypt_char(c, d, n) for c in ciphertext])

print(f"Decrypted Message: {decrypted_message}")

"""