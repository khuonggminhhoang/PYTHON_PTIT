from math import *

class SinhVien:
    cnt = 0

    def __init__(self, name, m1, m2, m3):
        SinhVien.cnt += 1
        self.__id = f'SV{SinhVien.cnt:02d}'
        self.__name = self.name_std(name)
        self.__m1 = m1
        self.__m2 = m2
        self.__m3 = m3

    def get_id(self):
        return self.__id

    def get_avg(self):
        return (self.__m1 * 3 + self.__m2 * 3 + self.__m3 * 2)/8
    
    def set_rank(self, rank):
        self.__rank = rank

    def get_rank(self):
        return self.__rank

    def name_std(self, name):
        arr = name.strip().title().split()
        return ' '.join(arr)

    def __str__(self):
        rnd = ceil(self.get_avg() * 100)/100
        return f'{self.__id} {self.__name} {rnd:.2f} {self.__rank}'

if __name__ == '__main__':
    t = int(input())
    lst = []
    for _ in range(t):
        lst.append(SinhVien(input(), float(input()), float(input()), float(input())))

    lst.sort(key= lambda x : (-x.get_avg(), x.get_id()))
    lst[0].set_rank(1)
    for i in range(1, t):
        if lst[i-1].get_avg() == lst[i].get_avg():
            lst[i].set_rank(lst[i-1].get_rank())
        else:
            lst[i].set_rank(i + 1)
    for x in lst:
        print(x)

