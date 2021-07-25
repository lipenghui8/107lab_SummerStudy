class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q
    def __add__(self, r):
        return Rational(self.p * r.q + self.q * r.p, self.q * r.q)
    def __sub__(self, r):
        return Rational(self.p*r.q-self.q*r.p,self.q*r.q)
    def __mul__(self, r):
        return Rational(self.p*r.p,self.q*r.q)
    def __truediv__(self, r):
        return Rational(self.p*r.q,self.q*r.p)
    def __str__(self):
        return '{}/{}'.format(self.p, self.q)
r1 = Rational(1, 2)
r2 = Rational(2, 3)
print(r1+r2)
print(r1-r2)
print(r1*r2)
print(r1/r2)

