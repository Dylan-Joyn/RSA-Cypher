from rsa_keys import *
from math_algorithms import *

def test_rsa_key_generation():
    keys = RSAKeys(bits=32)  # small primes for testing
    # Check gcd(e, phi) = 1
    assert gcd(keys.e, keys.phi) == 1
    # Check that n = p * q
    assert keys.n == keys.p * keys.q
    # Check that modular inverse works
    assert (keys.d * keys.e) % keys.phi == 1

