import random

### ---------------- math_algorithms ---------------- ###

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

### ---------------- rsa_keys ---------------- ###

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

### ---------------- rsa_operations ---------------- ###

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

### ---------------- io_operations ---------------- ###

# storage for signatures and messages
digital_signatures = []
encrypt_messages = []

def program_loop(keys):
    while True:
        print("\nPlease select your user type:")
        print("1. A public user")
        print("2. The owner of the keys")
        print("3. Exit program")
        user_choice = input("Enter your choice: ")

        match user_choice:
            case "1":
                public_user(keys)
            case "2":
                owner_of_keys(keys)
            case "3":
                print("Exiting program.")
                return False
            case _:
                print("Please enter a valid option.")

def encrypt_text(keys):
    message_to_encrypt = input("Enter a message: ")
    # convert to ascii values in an array
    ascii_values_mte = [ord(c) for c in message_to_encrypt]

    # encryption
    encrypted_message = []
    for M in ascii_values_mte:
        encrypted_message.append(encrypt(M, keys.e, keys.n))
    print("Message encrypted and sent.")
    return encrypted_message

def decrypt_text(keys, encrypted_message):
    decrypted_message = []
    for c in encrypted_message:
        decrypted_message.append(decrypt(c, keys.d, keys.n))
    # convert from ascii to string
    message_to_decrypt = ''.join([chr(c) for c in decrypted_message])
    print("Decrypted Message:", message_to_decrypt)
    return message_to_decrypt

def public_user(keys):
    print("\nAs a public user, what would you like to do?")
    print("1. Send an encrypted message")
    print("2. Authenticate a digital signature")
    print("3. Exit")
    user_choice = input("Enter your choice: ")
    match user_choice:
        case "1":
            encrypt_messages.append(encrypt_text(keys))
            public_user(keys)
        case "2": 
            if len(digital_signatures) == 0:
                print("There are no signatures to authenticate.")
            else:
                print("The following signed messages are available:")
                for i, (msg, sig) in enumerate(digital_signatures, start=1):
                    print(f"{i}. {msg}")

                signature_select = int(input("Enter your choice: ")) - 1
                msg, sig = digital_signatures[signature_select]  # unpack tuple (message, signature)

                # verify each character/signature pair
                verified = all(
                    verify(sig[i], ord(m), keys.e, keys.n)
                    for i, m in enumerate(msg)
                )  

                if verified:
                    print("Signature is valid")
                else:
                    print("Signature is not valid")
                    public_user(keys)
        case "3":
            return
        case _:
            print("Please enter a valid option.")

def owner_of_keys(keys):
    while True:
        print("\nAs the owner of the keys, what would you like to do?")
        print("1. Decrypt a received message")
        print("2. Digitally sign a message")
        print("3. Show the keys")
        print("4. Generate a new set of keys")
        print("5. Exit")
        user_choice = input("Enter your choice: ")

        match user_choice:
            case "1":
                print("The following messages are abailable: ")
                for i, msg in enumerate(encrypt_messages, start=0):
                    print(f"{(i+1)}. (length = {len(msg)})")
                select_em = int(input("Enter your choice: "))-1
                encrypt_message = encrypt_messages[select_em]
                decrypt_text(keys, encrypt_message)

            case "2":
                msg = input("Enter a message to sign: ")
                sig = [sign(ord(c), keys.d, keys.n) for c in msg]
                digital_signatures.append((msg, sig))
                print("Message signed and sent.")

            case "3":
                print("\n--- Current RSA Keys ---")
                print(f"Public Key (e, n): ({keys.e}, {keys.n})")
                print(f"Private Key (d, n): ({keys.d}, {keys.n})")
                print(f"p: {keys.p}")
                print(f"q: {keys.q}")
                print(f"phi: {keys.phi}")
                print("-------------------------")

            case "4":
                print("Generating a new set of keys...")
                new_keys = RSAKeys()
                keys.p, keys.q = new_keys.p, new_keys.q
                keys.n, keys.phi = new_keys.n, new_keys.phi
                keys.e, keys.d = new_keys.e, new_keys.d
                print("New keys generated successfully!")

            case "5":
                return

            case _:
                print("Please enter a valid option.")

### ---------------- main ---------------- ###

if __name__ == "__main__":
    user_choice = 0
    digital_signatures = []

    #generate keys
    keys = RSAKeys(bits=512)
    print("RSA keys have been generated.")

    activeInput = True
    while activeInput:
        #take in user input
        activeInput = program_loop(keys)
