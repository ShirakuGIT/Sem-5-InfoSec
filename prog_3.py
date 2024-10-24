"""
3. Use the Playfair cipher to encipher the message "The key is hidden
under the door pad". The secret key can be made by filling the first and
part of the second row with the word "GUIDANCE" and filling the rest of
the matrix with the rest of the alphabet.
"""

def generate_playfair_matrix(key):
    matrix = []
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # No 'J' in Playfair cipher
    used_letters = set()

    # Add key to matrix
    for char in key.upper():
        if char not in used_letters and char in alphabet:
            matrix.append(char)
            used_letters.add(char)

    # Fill the rest of the matrix with the unused alphabet letters
    for char in alphabet:
        if char not in used_letters:
            matrix.append(char)
            used_letters.add(char)

    return [matrix[i:i + 5] for i in range(0, 25, 5)]

def playfair_cipher_encrypt(message, matrix):
    message = message.replace(" ", "").upper().replace("J", "I")
    if len(message) % 2 != 0:
        message += 'X'  # Padding if necessary

    def find_position(char):
        for i, row in enumerate(matrix):
            if char in row:
                return i, row.index(char)
        return None, None

    encrypted_message = ""
    for i in range(0, len(message), 2):
        a, b = message[i], message[i + 1]
        row_a, col_a = find_position(a)
        row_b, col_b = find_position(b)

        if row_a == row_b:
            # Same row: shift to the right
            encrypted_message += matrix[row_a][(col_a + 1) % 5] + matrix[row_b][(col_b + 1) % 5]
        elif col_a == col_b:
            # Same column: shift down
            encrypted_message += matrix[(row_a + 1) % 5][col_a] + matrix[(row_b + 1) % 5][col_b]
        else:
            # Rectangle case: swap columns
            encrypted_message += matrix[row_a][col_b] + matrix[row_b][col_a]

    return encrypted_message

def playfair_cipher_decrypt(ciphertext, matrix):
    def find_position(char):
        for i, row in enumerate(matrix):
            if char in row:
                return i, row.index(char)
        return None, None

    decrypted_message = ""
    for i in range(0, len(ciphertext), 2):
        a, b = ciphertext[i], ciphertext[i + 1]
        row_a, col_a = find_position(a)
        row_b, col_b = find_position(b)

        if row_a == row_b:
            # Same row: shift to the left
            decrypted_message += matrix[row_a][(col_a - 1) % 5] + matrix[row_b][(col_b - 1) % 5]
        elif col_a == col_b:
            # Same column: shift up
            decrypted_message += matrix[(row_a - 1) % 5][col_a] + matrix[(row_b - 1) % 5][col_b]
        else:
            # Rectangle case: swap columns
            decrypted_message += matrix[row_a][col_b] + matrix[row_b][col_a]

    return decrypted_message

# Function to print Playfair matrix
def print_matrix(matrix):
    print("Playfair Cipher Matrix:")
    for row in matrix:
        print(" ".join(row))

# Generate Playfair matrix
key = "GUIDANCE"
matrix = generate_playfair_matrix(key)

# Print the matrix
print_matrix(matrix)

# Message to encrypt
message = "The key is hidden under the door pad"
ciphertext = playfair_cipher_encrypt(message, matrix)

# Print the ciphertext
print(f"\nPlayfair Cipher Ciphertext: {ciphertext}")

# Decrypt the ciphertext
decrypted_message = playfair_cipher_decrypt(ciphertext, matrix)

# Print the decrypted message
print(f"Decrypted Message: {decrypted_message}")
