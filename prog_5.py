"""
Encrypt the message "Confidential Data" using DES with the following
key: "A1B2C3D4". Then decrypt the ciphertext to verify the original
message.
"""

from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

# DES key and message
key = b'A1B2C3D4'  # Must be exactly 8 bytes
message = b'Confidential Data'

# Encrypt the message
cipher = DES.new(key, DES.MODE_ECB)
ciphertext = cipher.encrypt(pad(message, DES.block_size))

# Decrypt the message
decrypted_message = unpad(cipher.decrypt(ciphertext), DES.block_size)

print(f"Ciphertext: {ciphertext}")
print(f"Decrypted message: {decrypted_message.decode()}")
