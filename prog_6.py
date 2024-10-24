"""
Encrypt the message "Sensitive Information" using AES-128 with the
following
key:
"0123456789ABCDEF0123456789ABCDEF".
Then
decrypt the ciphertext to verify the original message.
"""

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# AES key and message
key = bytes.fromhex('0123456789ABCDEF0123456789ABCDEF')
message = b'Sensitive Information'

# Encrypt the message using AES-128
cipher = AES.new(key, AES.MODE_ECB)
ciphertext = cipher.encrypt(pad(message, AES.block_size))

# Decrypt the message
decrypted_message = unpad(cipher.decrypt(ciphertext), AES.block_size)

print(f"Ciphertext: {ciphertext.hex()}")
print(f"Decrypted message: {decrypted_message.decode()}")

