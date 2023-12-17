class NhanVien:
    cnt = 0

    def __init__(self, name, sal, workday, pos):
        NhanVien.cnt += 1
        self.__id = 'NV' + '{:02d}'.format(NhanVien.cnt)
        self.__name = name
        self.__sal = sal
        self.__workday = workday
        self.__pos = pos

    def getAllowance(self):
        s = self.__pos
        if s == 'GD': return 250000
        elif s == 'PGD': return 200000
        elif s == 'TP': return 180000
        else: return 150000

    def getAward(self):
        tmp = self.__workday
        if tmp >= 25: return 0.2
        elif tmp >= 22: return 0.1
        else: return 0
    
    def income(self):
        return self.__sal * self.__workday * (1 + self.getAward()) + self.getAllowance()

    def __str__(self):
        return f'{self.__id} {self.__name} {self.__sal * self.__workday} {self.getAward()} {self.getAllowance()} {self.income()}'

if __name__ == '__main__':
    nv = NhanVien(input(), int(input()), int(input()), input())
    print(nv)