from random import randint

class Random:
    def __init__(self, modulus):
        self.m = modulus
        self.init = randint(1, self.m)
        self.coef = [randint(1, self.m) for _ in range(8)]
        for _ in range(10): self.generate()
            
    def generate(self):
        val = 0
        for i in range(8):
            val += self.coef[i] * pow(self.init, i, self.m) % self.m
        self.init = val % self.m
        return self.init