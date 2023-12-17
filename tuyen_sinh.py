class SinhVien:
    def __init__(self, id, name, math, phys, chem):
        self.__id = id
        self.__name = name
        self.__math = math
        self.__phys = phys
        self.__chem = chem

    def pri(self):
        n = int(self.__id[2])
        if n == 1: return 0.5
        elif n == 2: return 1.0
        elif n == 3: return 2.5
        else: return 0
    
    def sum(self):
        return self.__math + self.__phys + self.__chem + self.pri()

    def __str__(self):
        tmp = ('TRUOT' if self.sum() < 24 else 'TRUNG TUYEN')
        return f'{self.__id} {self.__name} {self.__id[2]} {self.sum():.1f} {tmp}'

if __name__ == '__main__':
    sv = SinhVien(input(), input(), float(input()), float(input()), float(input()))
    print(sv)