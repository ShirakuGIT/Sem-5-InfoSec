"""
Use a Hill cipher to encipher the message "We live in an insecureworld". Use the following key:
K = [03 03 2 07]
"""

import numpy as np

# Hill Cipher Key (2x2 matrix)
K = np.array([[3, 3], [2, 7]])

# Message to encrypt (block size of 2, so we remove spaces and ensure even length)
message = "We live in an insecureworld".replace(" ", "").upper()
if len(message) % 2 != 0:
    message += 'X'  # Add padding if odd-length message

# Convert message to numbers (A=0, B=1, ..., Z=25)
message_nums = [ord(char) - ord('A') for char in message]

# Reshape message into 2xN blocks
message_pairs = np.array(message_nums).reshape(-1, 2)

# Encrypt each block using matrix multiplication and mod 26
ciphertext = ""
for pair in message_pairs:
    encrypted_pair = np.dot(K, pair) % 26
    ciphertext += ''.join([chr(num + ord('A')) for num in encrypted_pair])

print(f"Ciphertext: {ciphertext}")
