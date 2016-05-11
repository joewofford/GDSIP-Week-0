def gcd(a, b):
    '''
    INPUT: int, int
    OUTPUT: int

    Return the greatest common divisor of the two integers given.
    '''
    while a != 0:
        c = a
        a = b % a
        b = c
    return b


class Fraction(object):
    '''
    A fraction class.
    '''

    def __init__(self, pre, num, denom):
        '''
        Initialize a fraction with the given numerator and denominator.
        '''
        self.pre = pre
        self.num = num
        self.denom = denom
        self._reduce()
        self._unmix()

    def _reduce(self):
        '''
        Put the fraction in reduced form.
        '''
        if self.num == 0:
            self.denom = 1
        else:
            d = gcd(self.num, self.denom)
            if (self.denom / d) < 0: d = -1 * d
            self.num, self.denom = self.num / d, self.denom / d
        return self

    def _unmix(self):
        if self.num >= self.denom:
            self.pre += (self.num - self.num % self.denom) / self.denom
            self.num = self.num % self.denom


    def _mix(self):
        if self.pre != 0:
            self.num += self.pre * self.denom
            self.pre = 0

    def __add__(self, other):
        '''
        INPUT:
            - other: Fraction
        Return a fraction that is the sum of this fraction and other.
        '''
        return Fraction(self.pre + other.pre, self.num * other.denom + other.num * self.denom, self.denom * other.denom)

    def __sub__(self, other):
        '''
        INPUT:
            - other: Fraction
        Return a fraction that is the difference of this fraction and other.
        '''
        return Fraction(self.pre - other.pre, self.num * other.denom - other.num * self.denom, self.denom * other.denom)

    def __mul__(self, other):
        '''
        INTPUT:
            - other: Fraction or int
        Return a fraction that is the product of this fraction and other.
        '''
        self._mix()
        if isinstance(other, int):
            return Fraction(0, self.num * other, self.denom)
        other._mix()
        return Fraction(0, self.num * other.num, self.denom * other.denom)

    def __cmp__(self, other):
        '''
        INPUT:
            - other: Fraction
        Return 0 if equal, -1 if self < other, +1 if self > other
        '''
        return cmp((self - other).num, 0)

    def __repr__(self):
        '''
        Return a string representation of the fraction.
        '''
        if self.num == 0:
            return str(self.pre)
        if self.pre == 0:
            return "{0}/{1}".format(self.num, self.denom)
        else:
            return "{0} {1}/{2}".format(self.pre, self.num, self.denom)
