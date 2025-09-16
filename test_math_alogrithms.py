from math_algorithms import gcd, mod_inverse, mod_exp


def test_gcd():
    assert gcd(12, 8) ==4
    assert gcd(17, 13) ==1

def test_mod_inverse():
    assert mod_inverse(3, 11) ==4

def test_mod_exp():
    assert mod_exp(2,5,13)==6
