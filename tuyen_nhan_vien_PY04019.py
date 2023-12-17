class NhanVien:
    cnt  = 0
    
    def __init__(self, name, theory, prac):
        NhanVien.cnt += 1
        self.__id = f'TS{NhanVien.cnt:02d}'
        self.__name = name
        self.__theory = (theory/10) if theory > 10 else theory
        self.__prac = (prac/10) if prac > 10 else prac

    def get_id(self):
        return self.__id

    def avg(self):
        return (self.__theory + self.__prac)/2

    def classify(self):
        tmp = self.avg()
        if tmp < 5: return 'TRUOT'
        elif tmp < 8: return 'CAN NHAC'
        elif tmp <= 9.5: return 'DAT'
        else: return 'XUAT SAC'

    def __str__(self):
        return f'{self.__id} {self.__name} {self.avg():.2f} {self.classify()}'


if __name__ == '__main__':
    t = int(input())
    a = []
    while t:
        a.append(NhanVien(input(), float(input()), float(input())))
        t -= 1
    a.sort(key= lambda x : (-x.avg()))
    for x in a:
        print(x)