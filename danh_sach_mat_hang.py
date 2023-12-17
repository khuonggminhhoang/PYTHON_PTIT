from functools import cmp_to_key

class MatHang:
    cnt = 0

    def __init__(self, name, unit, purchase, price):
        MatHang.cnt += 1
        self.__id = f'MH{MatHang.cnt:04d}'
        self.__name = name
        self.__unit = unit
        self.__purchase = purchase
        self.__price = price

    def getId(self):
        return self.__id

    def benifit(self):
        return self.__price - self.__purchase
    
    def __str__(self):
        return f'{self.__id} {self.__name} {self.__unit} {self.__purchase} {self.__price} {self.benifit()}'


def cmp(o1, o2):
    if o1.benifit() != o2.benifit():
        return o2.benifit() - o1.benifit()
    elif o1.getId() < o2.getId():
        return -1
    else:
        return 1
        
if __name__ == '__main__':
    t = int(input())
    arr = []
    while t:
        arr.append(MatHang(input(), input(), int(input()), int(input()) ))
        t -= 1
    arr.sort(key= cmp_to_key(cmp))
    for x in arr:
        print(x)

