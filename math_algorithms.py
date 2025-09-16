import random


###checks if n is truly a prime number###
def is_prime(n, k=10):
    ###Miller-Rabin primality test - much faster for large numbers###
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    # Write n-1 as 2^r * d
    r = 0
    d = n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Witness loop
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)  # Use built-in pow for modular exponentiation

        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def generate_prime(bits):
    while True:

        p = random.getrandbits(bits)

        p |= (1 << bits-1) | 1  # Ensure it's odd and has correct bit length

        if is_prime(p):
            return p

def gcd(a, b):
    ###finds the greatest common divisor using Euclidean algorithm###
    while b:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    ###takes the extended Euclidean algorithm and uses it to find the modular inverse of e modulo phi###
    def extended_gcd(a,b):
        if a == 0:
            return b, 0, 1
        gcd_value, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd_value, x, y

    gcd_value,x, _= extended_gcd(e, phi)
    return (x % phi + phi) % phi

def mod_exp(base, exp, mod):
    ###finds (base ** exp) % mod using squaring###
    return pow(base, exp, mod)



