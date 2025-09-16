from rsa_operations import *

def test_encrypt_decrypt():
    n, e, d = 55, 3, 27  # sample RSA small key
    M = 7
    C = encrypt(M, e, n)
    assert decrypt(C, d, n) == M

def test_sign_verify():
    n, e, d = 55, 3, 27
    M = 7
    s = sign(M, d, n)
    assert verify(s, M, e, n)
