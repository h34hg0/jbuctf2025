from Crypto.Util.number import getPrime, bytes_to_long
from random import getrandbits

flag = bytes_to_long(open('./flag', 'rb').read())

e = 65537
p, q, r = getPrime(1024), getPrime(1024), getPrime(1024)

x = getrandbits(928)
a, b = pow(x, 2, p), pow(x, 2, q)
N = q * r
enc = pow(flag, e, N)

def noise(n):
    return n ^ getrandbits(1024)

x, q, r = noise(x), noise(q), noise(r)

with open("./output.txt","w+") as f:
    f.write(f'{e=}\n')
    f.write(f'{x=}\n')
    f.write(f'{p=}\n')
    f.write(f'{q=}\n')
    f.write(f'{r=}\n')
    f.write(f'{a=}\n')
    f.write(f'{b=}\n')
    f.write(f'{N=}\n')
    f.write(f'{enc=}\n')


