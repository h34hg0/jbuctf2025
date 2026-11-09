from Cipher import Cipher
from Crypto.Util.number import bytes_to_long
from Crypto.Random import get_random_bytes

cipher = Cipher(1024)
secret = get_random_bytes(240)
se = secret[0:80] + b'\x00'*160
cr = secret[80:160] + b'\x00'*80
et = secret[160:240]
assert bytes_to_long(secret) == bytes_to_long(se) + bytes_to_long(cr) + bytes_to_long(et)

print(f'N = {cipher.N}')
print(f'Enc(se) = {cipher.encrypt(se).hex()}')
print(f'Enc(cr) = {cipher.encrypt(cr).hex()}')
print(f'Enc(et) = {cipher.encrypt(et).hex()}')

i = input(f'Input (e, d): ')
    
if i == 'e':
    m = input('Input hex string to encrypt: ')
    m = bytes.fromhex(m)
    c = cipher.encrypt(m)
    print(f'Enc = {c.hex()}')
    
elif i == 'd':
    c = input('Input hex string to decrypt: ')
    c = bytes.fromhex(c)
    m = cipher.decrypt(c)
    print(f'Dec = {m.hex()}')
    
answer = input('Input secret: ')
answer = bytes.fromhex(answer)
if answer == secret:
    flag = open('./flag', 'rb').read().decode()
    print(flag)
else:
    print('Wrong!!')

