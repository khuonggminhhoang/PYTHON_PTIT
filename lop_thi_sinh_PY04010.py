class ThiSinh:
    def __init__(self, name, dob, m1, m2, m3):
        self.__name = name
        self.__dob = self.day_std(dob)
        self.__m1 = m1
        self.__m2 = m2
        self.__m3 = m3

    def day_std(self, s):
        if s[1] == '/':
            s = '0' + s
        if s[4] == '/':
            s = s[:3] + '0' + s[3:]
        return s

    def __str__(self):
        return f'{self.__name} {self.__dob} {self.__m1 + self.__m2 + self.__m3 :.1f}'

if __name__ == '__main__':
    ts = ThiSinh(input(), input(), float(input()), float(input()), float(input()))
    print(ts)

