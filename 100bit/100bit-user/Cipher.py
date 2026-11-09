from Crypto.Util.number import getPrime, long_to_bytes, GCD
from Crypto.Random import get_random_bytes
from random import randrange

def getCoprime(x):
	r = randrange(2, x-2)
	while GCD(x, r) != 1:
		r = randrange(2, x-2)
	return r

class Cipher: 
	def __init__(self):
		self.bit_len = 100
		self.privKey, self.pubKey = self.keyGen()

	def keyGen(self):
		bit_len = self.bit_len
		W = [randrange(1, 2**bit_len)]
		for i in range(1, bit_len):
			W.insert(i, randrange(((2**i)-1)*(2**bit_len)+1, (2**i)*(2**bit_len)))
		q = randrange(sum(W)+1, sum(W)*2 + 1)
		r = getCoprime(q)
		B = []
		for i in range(self.bit_len):
			B.insert(i, (r*W[i]) % q)

		privKey, pubKey = (W, r, q), B
		return privKey, pubKey

	def encrypt(self, bits, pubKey): 
		assert self.bit_len == len(bits), "Length of bits does not match the expected bit length."
		 
		ciphertext = 0
		for i in range(self.bit_len):
			ciphertext += int(bits[i]) * pubKey[i]
		return ciphertext

	def decrypt(self, ciphertext, privKey):
		W, r, q = self.privKey
		r_inv = pow(r, -1, q)
		C = (ciphertext * r_inv) % q 
		bits = ''

		for i in reversed(range(self.bit_len)):
			if C >= W[i]:
				C -= W[i]
				bits = '1' + bits
			else:
				bits = '0' + bits
				continue

		return bits

if __name__ == '__main__':
	from random import randint
	def test():
		for _ in range(10000):
			m = ''
			for _ in range(100):
				m += str(randint(0, 1))
			cipher = Cipher()
			ciphertext = cipher.encrypt(m, cipher.pubKey)
			assert m == cipher.decrypt(ciphertext, cipher.privKey), 'Test Failed'

		print('Tesest Passed')
	
	test()