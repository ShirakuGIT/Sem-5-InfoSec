"""
Design a Python-based experiment to analyze the performance of MD5,SHA-1, and
SHA-256 hashing techniques in terms of computation time and collision
resistance. Generate a dataset of random strings ranging from 50 to 100 strings,
compute the hash values using each hashing technique, and measure the time
taken for hash computation. Implementcollision detection algorithms to identify
any collisions within the hashed dataset.
"""

import hashlib
import random
import string
import time

# Generate random strings
def generate_random_strings(n, length):
    random_strings = []
    for _ in range(n):
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        random_strings.append(random_string)
    return random_strings

# Measure hashing time for a specific algorithm
def measure_hash_time(algorithm, data):
    start_time = time.time()
    hashed_values = [algorithm(s.encode()).hexdigest() for s in data]
    return time.time() - start_time, hashed_values

# Collision detection algorithm
def detect_collisions(hashed_values):
    seen = set()
    collisions = 0
    for h in hashed_values:
        if h in seen:
            collisions += 1
        seen.add(h)
    return collisions

# Experiment
random_strings = generate_random_strings(100, 50)  # 100 random strings of length 50

# Measure performance for MD5
md5_time, md5_hashes = measure_hash_time(hashlib.md5, random_strings)
md5_collisions = detect_collisions(md5_hashes)

# Measure performance for SHA-1
sha1_time, sha1_hashes = measure_hash_time(hashlib.sha1, random_strings)
sha1_collisions = detect_collisions(sha1_hashes)

# Measure performance for SHA-256
sha256_time, sha256_hashes = measure_hash_time(hashlib.sha256, random_strings)
sha256_collisions = detect_collisions(sha256_hashes)

# Display results
print(f"MD5 Time: {md5_time:.6f} seconds, Collisions: {md5_collisions}")
print(f"SHA-1 Time: {sha1_time:.6f} seconds, Collisions: {sha1_collisions}")
print(f"SHA-256 Time: {sha256_time:.6f} seconds, Collisions: {sha256_collisions}")
