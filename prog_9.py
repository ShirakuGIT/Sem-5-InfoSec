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

"""
import rsa

# Public key
n = 323
e = 5

# Private key
d = 173

# Message to encrypt
message = "Cryptographic Protocols"

# Split the message into chunks that can fit into 'n'
chunk_size = (n.bit_length() - 1) // 8  # Calculate the max chunk size
message_bytes = message.encode('utf-8')

# Function to split message into chunks
def split_into_chunks(data, chunk_size):
    return [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]

# Encrypt each chunk
ciphertext_chunks = []
for chunk in split_into_chunks(message_bytes, chunk_size):
    message_int = int.from_bytes(chunk, byteorder='big')
    ciphertext_chunk = pow(message_int, e, n)
    ciphertext_chunks.append(ciphertext_chunk)

# Decrypt each chunk
decrypted_bytes = b""
for ciphertext_chunk in ciphertext_chunks:
    decrypted_int = pow(ciphertext_chunk, d, n)
    decrypted_chunk = decrypted_int.to_bytes((decrypted_int.bit_length() + 7) // 8, byteorder='big')
    decrypted_bytes += decrypted_chunk

# Convert decrypted bytes back to string
decrypted_message = decrypted_bytes.decode('utf-8')

print(f"Encrypted: {ciphertext_chunks}")
print(f"Decrypted: {decrypted_message}")
"""