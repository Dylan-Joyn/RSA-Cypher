from rsa_operations import *
from rsa_keys import *

#generate keys
keys = RSAKeys(bits=512)

#take in user input
message_to_encrypt = input("Please enter your message: ")

#convert to ascii values in an array
ascii_values_mte = [ord(c) for c in message_to_encrypt]

#encryption
encrypted_message = []
for c in message_to_encrypt:
    M = ord(c)
    encrypted_message.append(encrypt(M, keys.e, keys.n))

print("Encrypted Message: ", encrypted_message)

#decryption
decrypted_message = []
for c in encrypted_message:
    decrypted_message.append(decrypt(c, keys.d, keys.n))

print("Decrypted Message in ASCII: ", decrypted_message)

#convert from ascii to string
message_to_decrypt = ''.join([chr(c) for c in decrypted_message])

print("Final Decrypted Message: ", message_to_decrypt)
