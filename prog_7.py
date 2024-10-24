"""
With the ElGamal public key (p = 7919, g = 2, h = 6465) and the private
key x = 2999, encryptthe message "Asymmetric Algorithms". Decrypt
the resulting ciphertext to verify the originalmessage.
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
from Crypto.PublicKey import ElGamal
from Crypto.Random import random
from Crypto.Util.number import bytes_to_long, long_to_bytes

# ElGamal key parameters
p = 7919
g = 2
h = 6465
x = 2999

# Construct ElGamal public and private keys
public_key = ElGamal.construct((p, g, h))
private_key = ElGamal.construct((p, g, h, x))

# Message to encrypt
message = "Asymmetric Algorithms"
message_bytes = message.encode('utf-8')
message_int = bytes_to_long(message_bytes)

# Ensure message_int < p
if message_int >= p:
    raise ValueError("Message too long for the key size.")

# ElGamal Encryption
k = random.StrongRandom().randint(1, p - 2)
ciphertext = public_key.encrypt(message_int, k)[0]

print(f"Encrypted: {ciphertext}")

# ElGamal Decryption
decrypted_int = private_key.decrypt(ciphertext)
decrypted_bytes = long_to_bytes(decrypted_int)
decrypted_message = decrypted_bytes.decode('utf-8')

print(f"Decrypted: {decrypted_message}")

"""

"""
from Crypto.PublicKey import ElGamal
from Crypto.Random import random
from Crypto.Util.number import bytes_to_long, long_to_bytes

# ElGamal key parameters
p = 7919  # A prime number
g = 2     # A generator in the multiplicative group of integers modulo p
h = 6465  # h = g^x mod p, where x is the private key
x = 2999  # Private key

# Construct ElGamal public and private keys
public_key = ElGamal.construct((p, g, h))
private_key = ElGamal.construct((p, g, h, x))

# Message to encrypt
message = "Asymmetric Algorithms"
message_bytes = message.encode('utf-8')
message_int = bytes_to_long(message_bytes)

# Ensure the message integer is less than p
if message_int >= p:
    raise ValueError("Message too long for the key size.")

# ElGamal Encryption
k = random.StrongRandom().randint(1, p - 2)  # Random ephemeral key
ciphertext = public_key.encrypt(message_int, k)

print(f"Encrypted Ciphertext: {ciphertext}")

# ElGamal Decryption
decrypted_int = private_key.decrypt(ciphertext)
decrypted_bytes = long_to_bytes(decrypted_int)
decrypted_message = decrypted_bytes.decode('utf-8')

print(f"Decrypted Message: {decrypted_message}")

"""