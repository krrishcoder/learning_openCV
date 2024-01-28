from sympy import mod_inverse, isprime
from math import isqrt

def factorize(n):
    # A simple factorization method; you may want to use a more sophisticated one for large numbers
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return i, n // i

n = 64064959164923876064
e = 65537
c = 62499128160674246865

# Try to factorize n
factors = factorize(n)

print("test 1")

if factors is not None and all(isprime(factor) for factor in factors):
    p, q = factors
    phi = (p - 1) * (q - 1)
    d = mod_inverse(e, phi)

    print("test 2")
    
    # Decrypt the ciphertext
    m = pow(c, d, n)

    print("test 3")
    
    # Convert the decrypted message to bytes and then to a string
    decrypted_message = m.to_bytes((m.bit_length() + 7) // 8, 'big').decode('utf-8')

    print("test 4")
    
    print(decrypted_message)
else:
    print("Factorization failed. Use a different approach to obtain the private key.")