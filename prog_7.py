"""
With the ElGamal public key (p = 7919, g = 2, h = 6465) and the private
key x = 2999, encryptthe message "Asymmetric Algorithms". Decrypt
the resulting ciphertext to verify the originalmessage.
"""

"""
import random

# Given ElGamal public key and private key
p = 7919
g = 2
h = 6465
x = 2999

# Message to encrypt (converted to integer)
message = "Asymmetric Algorithms"
message_int = [ord(char) for char in message]

# ElGamal Encryption
ciphertext = []
for m in message_int:
    y = random.randint(1, p - 2)  # Random integer
    c1 = pow(g, y, p)
    c2 = (m * pow(h, y, p)) % p
    ciphertext.append((c1, c2))

# ElGamal Decryption
decrypted_message = ""
for c1, c2 in ciphertext:
    s = pow(c1, x, p)
    m = (c2 * pow(s, p - 2, p)) % p  # Modular inverse of s
    decrypted_message += chr(m)

print(f"Ciphertext: {ciphertext}")
print(f"Decrypted message: {decrypted_message}")

"""
import elgamal

# Given ElGamal public key parameters
p = 7919
g = 2
h = 6465
x = 2999

# Initialize the ElGamal key
public_key = elgamal.PublicKey(p, g, h)
private_key = elgamal.PrivateKey(public_key, x)

# Message to encrypt
message = "Asymmetric Algorithms".encode()

# Encrypt the message
ciphertext = public_key.encrypt(message)
print(f"Ciphertext: {ciphertext}")

# Decrypt the message
decrypted_message = private_key.decrypt(ciphertext).decode()
print(f"Decrypted message: {decrypted_message}")

