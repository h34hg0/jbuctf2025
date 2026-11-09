from CurveP256 import CurveP256
from Random import Random

class ECDSA:
    def __init__(self, d):
        self.curve = CurveP256()
        self.random = Random(self.curve.n)
        if d > self.curve.n:
            raise ValueError('Private key must be less than the curve order')
        self.privKey = d
        self.pubKey = self.curve.mult(self.privKey, self.curve.G) 

    def sign(self, h):
        curve = self.curve
        n = self.curve.n
        k = self.random.generate()
        h = int(h.hex(), 16)

        tmp = curve.mult(k, curve.G)
        r = tmp.x % n
        s = ((h % n + r * self.privKey % n) * pow(k, -1, n)) % n
        return (r, s)

    def verify(self, h, sign):
        curve = self.curve
        n = curve.n
        h = int(h.hex(), 16)
        r, s = sign
        w = pow(s, -1, n)
        u = (w * (h % n)) % n
        v = w * r % n
        Q = curve.add(curve.mult(u, curve.G), curve.mult(v, self.pubKey)) # Q = kG
        if sign[0] == Q.x % n:
            return True

        return False

# Test ECDSA
if __name__ == '__main__':
    import os
    from Crypto.Hash import SHA256
    from random import randrange
    from tqdm import trange
    curve = CurveP256()
    
    ecdsa = ECDSA(randrange(1, curve.n))
    for i in trange(1000):
        
        m = os.urandom(randrange(100))
        h = SHA256.new(m).digest()

        sign = ecdsa.sign(h)
        if not ecdsa.verify(h, sign):
            print('Fail')
            break
    print('Success')
