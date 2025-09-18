from rsa_operations import *
from rsa_keys import *

# storage for signatures
digital_signatures = []

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
    return True


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
            encrypted_msg = encrypt_text(keys)
        case "2": 
            if len(digital_signatures) == 0:
                print("There are no signatures to authenticate.")
            else:
                print("The following signed messages are available:")
                for i, (msg, sig) in enumerate(digital_signatures, start=1):
                    print(f"{i}. {msg}")

                try:
                    signature_select = int(input("Enter your choice: "))
                    msg, sig = digital_signatures[signature_select - 1]
                    verified = all(
                        verify(ord(m), s, keys.e, keys.n)
                        for m, s in zip(msg, sig)
                    )
                    if verified:
                        print("Signature is valid")
                    else:
                        print("Signature is not valid")
                except (ValueError, IndexError):
                    print("Invalid selection.")
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
                # simulate receipt of an encrypted message
                encrypted_msg = encrypt_text(keys)  # in practice, this would be sent in
                decrypt_text(keys, encrypted_msg)

            case "2":
                msg = input("Enter a message to sign: ")
                sig = [sign(ord(c), keys.d, keys.n) for c in msg]
                digital_signatures.append((msg, sig))
                print("Message signed and stored.")

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
                new_keys = RSAKeys()   # regenerate with default 512-bit primes
                keys.p, keys.q = new_keys.p, new_keys.q
                keys.n, keys.phi = new_keys.n, new_keys.phi
                keys.e, keys.d = new_keys.e, new_keys.d
                print("✅ New keys generated successfully!")

            case "5":
                return  # exit owner menu

            case _:
                print("Please enter a valid option.")
