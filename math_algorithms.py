import random

###checks if n is truly a prime number###
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
        else:
            return True

def generate_prime(bits):
    ###generates a random prime number with 'bits' bits###
    while True:
        p = random.getrandbits(bits)
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
    result = 1
    while exp > 0:
        if exp % 2 ==1:
            result = (result * base) % mod
        exp >>= 1
        base = (base * base) % mod
    return result