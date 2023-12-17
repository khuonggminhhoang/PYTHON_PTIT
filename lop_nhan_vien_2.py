class NhanVien:
    def __init__(self, name, gender, dob, addr, taxcode, contract):
        self.__id = '00001'
        self.__name = self.nameStd(name)
        self.__gender = gender
        self.__dob = self.dayStd(dob)
        self.__addr = addr
        self.__taxcode = taxcode
        self.__contract = self.dayStd(contract)

    def nameStd(self, s):
        arr = s.strip().title().split()
        return ' '.join(arr)

    def dayStd(self, s):
        if s[1] == '/':
            s = '0' + s
        if s[4] == '/':
            s = s[0:3] + '0' + s[3:]
        return s
    
    def __str__(self):
        return f'{self.__id} {self.__name} {self.__gender} {self.__dob} {self.__addr} {self.__taxcode} {self.__contract}'

if __name__ == '__main__':
    nv = NhanVien(input(), input(), input(), input(), input(), input())
    print(nv)
