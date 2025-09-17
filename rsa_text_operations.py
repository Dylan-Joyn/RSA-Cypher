from rsa_operations import *
from rsa_keys import *
from io_operations import *

user_choice = 0
digital_signatures = []

#generate keys
keys = RSAKeys(bits=512)
print("RSA keys have been generated.")

activeInput = True
while activeInput:
    #take in user input
    activeInput = program_loop()