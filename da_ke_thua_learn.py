class A:
    def __init__(self, a):
        self._a = a

class B:
    def __init__(self, b):
        self._b = b

class C(A, B):
    def __init__(self, a, b):
        A.__init__(self, a)
        B.__init__(self, b)
    
    def show(self):
        print( f'{self._a} {self._b}')

if __name__ == '__main__':
    x = C(100, 200)
    x.show()
    a = A(12)