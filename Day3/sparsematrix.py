from collections import defaultdict


class SparseMatrix(object):
    def __init__(self, m, n, default=0):
        self.n = n
        self.m = m
        self.mat = defaultdict(dict)
        self.default = default

    def __getitem__(self, pair):
        if self._validate(pair):
            x, y = pair
            return self.mat[x].get(y, self.default)
        else:
            print 'Range error'
            return KeyError

    def __setitem__(self, pair, val):
        if self._validate(pair):
            x, y = pair
            self.mat[x][y] = val
        else:
            print 'Range error'
            return KeyError

    def __repr__(self):
        string = ''
        for x in xrange(self.m):
            for y in xrange(self.n):
                string = string + '\t' + str(round(float(self.mat[x].get(y, self.default)), 2))
            string = string + '\n'
        return string

    def _validate(self, pair):
        i, j = pair
        if i >= 0 and j >= 0:
            if (self.m - i) > 0 and (self.n - j) > 0:
                return True
        else:
            return False

    def fill_from_lists(self, lists):
        if len(lists) != self.m or len(lists[0]) != self.n:
            return 'Dimension Error: lists do not match matrix'
        for x in xrange(self.m):
            for y in xrange(self.n):
                self.mat[x][y] = lists[x][y]

    def sum(self):
        total = 0
        for x in xrange(self.m):
            total += sum(self.mat[x].values())
        return total

    def is_diagonal(self):
        if self.m != self.n:
            return False
        else:
            for x in xrange(self.m):
                for y in xrange(self.n):
                    if self.mat[x].get(y, self.default) != 0 and x != y:
                        return False
        return True
