class A:
    def __init__(self, a):
        self._a = a

class B(A):
    def __init__(self, b):
        self._b = b

class C(B):
    def __init__(self, a, b):
        A.__init__(self, a)
        B.__init__(self, b)

    def show(self):
        print(self._a, self._b)

if __name__ == '__main__':
    c = C(100, 200)
    c.show()

# note: tên biến phải là protected hoặc public  thì lớp con mới truy cập vào đc 