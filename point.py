from math import sqrt


class Point(object):
    '''
    A 2d point class
    '''
    def __init__(self, x, y):
        '''
        Initialize a point with the given x and y coordinate values.
        '''
        self.x = x
        self.y = y

    def __repr__(self):
        '''
        Return a string representation of the point.
        '''
        return "Point: {}, {}".format(str(self.x), str(self.y))

    def __eq__(self, other):
        '''
        INPUT:
            - other: Point
        Return True iff this is the same point as other.
        '''
        if self.x == other.x and self.y == other.y:
            return True
        return False

    def __add__(self, other):
        '''
        INPUT:
            - other: Point
        Return a new Point which adds the x and y coordinates of the two points
        together.
        '''
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        '''
        INPUT:
            - other: Point
        Return a new Point which subtracts the x and y coordinates of the second
        point from the first.
        '''
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        '''
        INPUT:
            - other: int/float
        Return a new Point which multiplies both the x and y coordinate values
        by the given value.
        '''
        return Point(self.x * other, self.y * other)

    def length(self):
        '''
        Return the length of the vector (squareroot of the two values squared)
        '''
        self.length = sqrt(self.x ** 2 + self.y ** 2)
        return self.length

    def dist(self, other):
        '''
        Return the distance (float) between this point and the other point given.
        '''
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


class Triangle(object):
    '''
    A 2d shape class, defined by three instances of the Point class
    '''

    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def perimeter(self):
        self.perimeter = self.p1.dist(self.p2) + self.p2.dist(self.p3) + self.p3.dist(self.p1)
        return self.perimeter

    def area(self):
        self.area = sqrt(self.perimeter/2 * (self.perimeter/2 - self.p1.dist(self.p2)) * (self.perimeter/2 - self.p2.dist(self.p3)) * (self.perimeter/2 - self.p3.dist(self.p1)))
        return self.area
