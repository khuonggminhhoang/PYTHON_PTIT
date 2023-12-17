class SinhVien:
    def __init__(self):
        pass

    def __init__(self, name, classs, dob, gpa):
        self.__id = 'SV001'
        self.__name = name
        self.__classs = classs
        self.__dob = self.dayStd(dob)
        self.__gpa = gpa

    def dayStd(self, s):
        if s[1] == '/':
            s = '0' + s
        if s[4] == '/':
            s = s[0:3] + '0' + s[3:]
        return s

    def __str__(self):
        return f'{self.__id} {self.__name} {self.__classs} {self.__dob} {self.__gpa:.1f}'


if __name__ == '__main__':
    sv = SinhVien(input(), input(), input(), float(input()))
    print(sv)