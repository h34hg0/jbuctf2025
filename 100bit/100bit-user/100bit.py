from Cipher import Cipher
from Crypto.Util.number import long_to_bytes

flag = open('./flag', 'r').read()
flag = flag[len('scpCTF{'):-len('}')]
assert flag == long_to_bytes(int(flag, 16)).hex()
print(hex(int(flag, 16)))
flag = bin(int(flag, 16))[2:]

while True:
    cipher = Cipher()
    pk = cipher.pubKey
    enc_flag = cipher.encrypt(flag, pk)
    i = input('Enter your choice: ')
    
    if i == '1':
        print(pk)
        print(enc_flag)
    
    elif i == '2':
        exit()

