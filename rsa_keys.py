from math_algorithms import *


class RSAKeys:
    def __init__(self, bits=512):

        ### get two distinct primes p and q ###
        self.p = generate_prime(bits)
        self.q = generate_prime(bits)
        while self.q == self.p:
            self.q = generate_prime(bits)

        ### n = p * q ###
        self.n = self.p * self.q

        ### phi(n) = (p-1)*(q-1) ###
        self.phi = (self.p - 1) * (self.q - 1)

        ### choose public exponent e such that gcd(e, phi) = 1 ###
        self.e = 3
        while gcd(self.e, self.phi) != 1:
            self.e += 2

        ### private exponent d (modular inverse of e modulo phi) ###
        self.d = mod_inverse(self.e, self.phi)


