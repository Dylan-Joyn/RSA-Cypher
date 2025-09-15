def gcd(p, q):
    while q:
        p, q = q, p % q
    return p

def extended_gcd(p,q):
    if p == 0:
        return q, 0, 1
    gcd_value, x1, y1 = extended_gcd(q % p, p)
    x = y1 - (q // p) * x1
    y = x1
    return gcd_value, x, y




if __name__ == '__main__':
    print()

