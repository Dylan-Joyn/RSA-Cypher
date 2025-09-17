from rsa_operations import *
from rsa_keys import *

def program_loop():
    print("Please select your user type:")
    print("1. A public user")
    print("2. The owner of the keys")
    print("3. Exit program ")
    user_choice = input("Enter your choice: ")
    match user_choice:
        case 1:
            public_user()
        case 2:
            #owner_of_keys
            print("to be implemented")
        case 3:
            return False
        case _:
            user_choice = input("Please enter a valid option: ")
    return True


def encrypt_text(keys):
    message_to_encrypt = input("Enter a message: ")
    #convert to ascii values in an array
    ascii_values_mte = [ord(c) for c in message_to_encrypt]

    #encryption
    encrypted_message = []
    for c in message_to_encrypt:
        M = ord(c)
        encrypted_message.append(encrypt(M, keys.e, keys.n))
        print("Message encrypted and sent.")
    return(encrypted_message)
    

#decryption
def decrypt_text(keys, encrypted_message):
    decrypted_message = []
    for c in encrypted_message:
        decrypted_message.append(decrypt(c, keys.d, keys.n))
    #convert from ascii to string
    message_to_decrypt = ''.join([chr(c) for c in decrypted_message])
    print("Decrypted Message: ", message_to_decrypt)

def public_user():
    print("As a public user, what would you like to do?")
    print("1. Send an encrypted message")
    print("2. Authenticate a digital signature")
    print("3. Exit ")
    user_choice = input("Enter your choice: ")
    match user_choice:
        case 1:
            encrypt_text(keys)
        case 2: 
            if(digital_signatures == []):
                print("There are no signature to authenticate. ")                
            else:
                print("The following messages are available:")
                i = 1
                for signature in digital_signatures:
                    print(i, ". ", signature)
                signature_select = input("Enter your choice: ")
                verify 

def 