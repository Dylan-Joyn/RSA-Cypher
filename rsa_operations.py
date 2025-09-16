from math_algorithms import *

def encrypt(M, e, n):
    ### encrypt integer M using public key (e, n) ###
    return mod_exp(M, e, n)


def decrypt(C, d, n):
    ### Decrypt integer C using private key (d, n) ###
    return mod_exp(C, d, n)


def sign(M, d, n):
    ### Sign integer M using private key (d, n) ###
    return mod_exp(M, d, n)


def verify(s, M, e, n):
    ### Verify that signature s corresponds to M using public key (e, n) ###
    return mod_exp(s, e, n) == M