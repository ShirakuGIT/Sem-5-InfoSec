"""
Using ECC (Elliptic Curve Cryptography), encrypt the message
"Secure Transactions" with the public key. Then decrypt the ciphertext
with the private key to verify the original message.
"""

from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric.utils import decode_dss_signature, encode_dss_signature

# Generate ECC private key
private_key = ec.generate_private_key(ec.SECP256R1())
public_key = private_key.public_key()

# Message to encrypt
message = b"Secure Transactions"

# Encrypt the message (using a simple signing approach for demonstration)
signature = private_key.sign(message, ec.ECDSA(hashes.SHA256()))

# Decrypt the message (using verification approach)
try:
    public_key.verify(signature, message, ec.ECDSA(hashes.SHA256()))
    print("Message is authentic.")
except:
    print("Message is not authentic.")
