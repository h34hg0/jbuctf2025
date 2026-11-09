from Crypto.Util.number import getPrime, GCD, bytes_to_long, long_to_bytes
from Crypto.Random import get_random_bytes
from random import randint

lcm = lambda a, b: a * b // GCD(a, b)    

class Cipher():
    def __init__(self, bits):
        self.P = getPrime(bits)
        self.Q = getPrime(bits)
        self.N = self.P * self.Q
        self.G = self.N + 1
        self.N2 = self.N ** 2
        self.La = lcm(self.P - 1, self.Q - 1)

    def encrypt(self, plaintext):
        m = bytes_to_long(plaintext)
        assert 0 <= m and m < self.N
        r = randint(1, self.N-1)
        ciphertext =  (pow(self.G, m, self.N2) * pow(r, self.N, self.N2)) % self.N2
        return long_to_bytes(ciphertext)
    
    def L(self, x):
        return (x-1) // self.N
    
    def decrypt(self, ciphertext):
        c = bytes_to_long(ciphertext)
        mu = self.L(pow(self.G, self.La, self.N2))
        mu = pow(mu, -1, self.N)
        ciphertext = (self.L(pow(c, self.La, self.N2)) * mu) % self.N
        return long_to_bytes(ciphertext)
    
if __name__ == '__main__':

    def test():
        for i in range(1000):
            cipher = Cipher(1024)
            m = get_random_bytes(240)
            c = cipher.encrypt(m)
            assert m == cipher.decrypt(c), 'Decryption failed'
        print(('All tests passed!'))
        
    test()