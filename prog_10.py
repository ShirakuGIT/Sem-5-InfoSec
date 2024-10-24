"""
Implement the hash function in Python. Your function should start withan initial
hash value of 5381 and for each character in the input string, multiply the current
hash value by 33, add the ASCII value of the character, and use bitwise operationsto ensure thorough mixing of the bits. Finally, ensure the hash value is kept within a
32-bit range by applying an appropriate mask.
"""

def custom_hash(input_string):
    # Start with an initial hash value of 5381
    hash_value = 5381
    
    # Loop through each character in the input string
    for char in input_string:
        # Multiply the current hash value by 33 and add the ASCII value of the character
        hash_value = ((hash_value * 33) + ord(char)) & 0xFFFFFFFF  # Keep within 32-bit range
    
    return hash_value

# Example usage
input_string = "Hashing Example"
hash_result = custom_hash(input_string)
print(f"Hash result: {hash_result}")
