from ECDSA import ECDSA
from Crypto.Hash import SHA256
from Crypto.Util.number import bytes_to_long, long_to_bytes

privKey = bytes_to_long(open('./flag', 'rb').read())
ds = ECDSA(privKey)

for i in range(10):
    with open(f'./files/lorem_ipsum{i+1}.txt', 'r') as text:
        m = text.read()
        h = SHA256.new(m.encode()).digest()
        sign = ds.sign(h)
        assert ds.verify(h, sign)

        with open(f'./signs/lorem_ipsum{i+1}_sign.txt', 'w') as sign_text:
            sign_text.write(f'{m}\n')
            sign_text.write(f'{h.hex()}\n')
            sign_text.write(f'{long_to_bytes(sign[0]).hex()}\n')
            sign_text.write(f'{long_to_bytes(sign[1]).hex()}\n')
