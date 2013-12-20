class Fraction(object):
    def __init__(self, num, den):
        _int_error_msg = u'Only integers are acceptable'
        if not isinstance(num, int):
            raise TypeError(_int_error_msg)
        if not isinstance(den, int):
            raise TypeError(_int_error_msg)

        if den < 0:
            den *= -1
            num *= -1

        g = self.gcd(num, den)
        num /= g
        den /= g
        self.num = int(num)
        self.den = int(den)

    @staticmethod
    def gcd(n,m):
        while m != 0:
            old_n = n
            old_m = m
            n = old_m
            m = old_n % old_m
        return n

    def __str__(self):
        return u'%s/%s' % (self.num, self.den)

    def __unicode__(self):
        return self.__str__()

    def __add__(self, other):
        new_num = self.num * other.den + self.den*other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __sub__(self, other):
        new_num = self.num * other.den - self.den * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __mul__(self, other):
        new_num = self.num * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __div__(self, other):
        new_num = self.num * other.den
        new_den = self.den * other.num
        return Fraction(new_num, new_den)

    def __gt__(self, other):
        return self.num * other.den > self.den * other.num

    def __ge__(self, other):
        return self.num * other.den >= self.den * other.num

    def __lt__(self, other):
        return self.num * other.den < self.den * other.num

    def __le__(self, other):
        return self.num * other.den <= self.den * other.num

    def __eq__(self, other):
        return self.num * other.den == self.den * other.num

    def __ne__(self, other):
        return self.num * other.den != self.den * other.num

    def __iadd__(self, other):
        return self + other

    def __repr__(self):
        return self.__str__()

    def get_num(self):
        return self.num

    def get_den(self):
        return self.den
