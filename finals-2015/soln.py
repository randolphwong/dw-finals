from libdw import sm

def cmp_list(l1, l2):
    return cmp(sorted(l1), sorted(l2)) == 0

def compTrace(A):
    '''A must be a square matrix'''
    if A == []: return 0
    if len(A) == 1: return A[0]
    return sum([A[i][i] for i in range(len(A))])

def test_compTrace():
    A = [[2.2, 2, 3.1], [4, 5, 6], [7, 8, 9]]
    print 'test_compTrace:', (compTrace(A) - 16.2) < 0.001
    A = [1]
    print 'test_compTrace:', (compTrace(A) - 1) < 0.001
    A = []
    print 'test_compTrace:', (compTrace(A) - 0) < 0.001

# method 1
def findKey(d, s):
    return [k for k, v in d.iteritems() if v == s]

# method 2
# def findKey(d, s):
    # results = []
    # for key in d:
        # if d[key] == s:
            # results.append(key)
    # return results

def test_findKey():
    dInput = {1:'singapore', 20:'china', 4:'japan', 5:'china', 10:'japan'}
    a = findKey(dInput, 'china')
    print 'test_findKey:', cmp_list(a, [5,20])
    print 'test_findKey:', findKey(dInput, 'korea') == []

class Square:

    def __init__(self, x=0, y=0, sideLength=1.0):
        self.x = x
        self.y = y
        self.sideLength = sideLength

    def getTopLeft(self):
        x = self.x - (self.sideLength / 2)
        y = self.y + (self.sideLength / 2)
        return x, y

    def getBtmRight(self):
        x = self.x + (self.sideLength / 2)
        y = self.y - (self.sideLength / 2)
        return x, y

    def getCenter(self):
        return self.x, self.y

    def getSideLength(self):
        return self.sideLength

    def getArea(self):
        return self.sideLength**2

    def getPerimeter(self):
        return self.sideLength * 4

    def containPoint(self, px, py):
        within_x = ((px >= self.x - self.sideLength / 2) and (px <= self.x + self.sideLength / 2))
        within_y = ((py >= self.y - self.sideLength / 2) and (py <= self.y + self.sideLength / 2))
        return within_x and within_y

    def containSquare(self, inSquare):
        top_left = inSquare.getTopLeft()
        btm_right = inSquare.getBtmRight()
        return self.containPoint(*top_left) and self.containPoint(*btm_right)

def test_square():
    s = Square(x=1,y=1, sideLength=2.0)
    print 'test_square:', s.getCenter() == (1, 1)
    print 'test_square:', s.getSideLength() == 2.0
    print 'test_square:', s.getArea() == 4.0
    print 'test_square:', s.getPerimeter() == 8.0
    print 'test_square:', s.containPoint(0,0) == True
    print 'test_square:', s.containPoint(0,-0.5) == False
    print 'test_square:', s.containPoint(1,1.5) == True
    print 'test_square:', s.containSquare( Square(x=1.5, y = 1, sideLength = 1)) == True
    print 'test_square:', s.containSquare( Square(x=1.5, y = 1, sideLength = 1.1)) == False
    s2 = Square()
    print 'test_square:', s2.getCenter() == (0, 0)
    print 'test_square:', s2.getSideLength() == 1.0
    print 'test_square:', s2.getPerimeter() == 4.

class Elevator(sm.SM):

    startState = 'First'

    def getNextValues(self, state, inp):
        sm = {'First': {'Up': 'Second', 'Down': 'First'},
              'Second': {'Up': 'Third', 'Down': 'First'},
              'Third': {'Up': 'Third', 'Down': 'Second'}}
        next_state = sm[state][inp]
        return next_state, next_state

def test_elevator():
    e = Elevator()
    print e.transduce( ['Up', 'Up', 'Up', 'Up', 'Down', 'Down', 'Down', 'Up'])

def countNumOpenLocker(K):
    lockers = [False] * K
    for i in range(K):
        for k in range(i, K, i + 1):
            lockers[k] = not lockers[k]
    return sum(lockers)

def test_countNumOpenLocker():
    print 'test_countNumOpenLocker', countNumOpenLocker(2000) == 44
    print 'test_countNumOpenLocker', countNumOpenLocker(10) == 3
    print 'test_countNumOpenLocker', countNumOpenLocker(20) == 4

test_compTrace()
test_findKey()
test_square()
test_elevator()
test_countNumOpenLocker()
