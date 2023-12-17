class SinhVien:
    cnt = 0

    def __init__(self, name, classs, dob, gpa):
        SinhVien.cnt += 1
        self.__id = f'SV{SinhVien.cnt:03d}'
        self.__name = name
        self.__dob = self.dayStd(dob)
        self.__classs = classs
        self.__gpa = gpa

    def dayStd(self, s):
        if s[1] == '/':
            s = '0' + s
        if s[4] == '/':
            s = s[0:3] + '0' + s[3:]
        return s
    
    def __str__(self):
        return f'{self.__id} {self.__name} {self.__classs} {self.__dob} {self.__gpa:.2f}'

if __name__ == '__main__':
    t = int(input())
    while t:
        sv = SinhVien(input(), input(), input(), float(input()))
        print(sv)
        t-= 1