class SinhVien:
    def __init__(self, name, dob, m1, m2, m3):
        self.__name = name
        self.__dob = self.dayStd(dob)
        self.__m1 = m1
        self.__m2 = m2
        self.__m3 = m3

    def dayStd(self, s):
        if s[1] == '/':
            s = '0' + s
        if s[4] == '/':
            s = s[0:3] + '0' + s[3:]
        return s

    def sum(self):
        return self.__m1 + self.__m2 + self.__m3
    
    def __str__(self):
        return f'{self.__name} {self.__dob} {self.sum():.1f}'

    

if __name__ == '__main__':
    sv = SinhVien(input(), input(), float(input()), float(input()), float(input()))
    print(sv)