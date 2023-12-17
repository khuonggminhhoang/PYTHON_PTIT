from functools import cmp_to_key

class SinhVien:
    def __init__(self, name, C, T):
        self.__name = name
        self.__C = C
        self.__T = T
    
    def getC(self):
        return self.__C
    
    def getT(self):
        return self.__T
    
    def getName(self):
        return self.__name

    def __str__(self):
        return self.__name + ' ' + str(self.__C) + ' ' + str(self.__T)

def cmp(o1, o2):
    if o1.getC() != o2.getC():
        return o2.getC() - o1.getC()
    elif o1.getT() != o2.getT():
        return o1.getT() - o2.getT()
    else:
        return (o1.getName() > o2.getName()) - (o1.getName() < o2.getName())

if __name__ == '__main__':
    n = int(input())
    arr = []
    for _ in range(n):
        name = input()
        C, T = map(int, input().split())
        arr.append(SinhVien(name, C, T))
    
    arr.sort(key=cmp_to_key(cmp))
    for x in arr:
        print(x)
    