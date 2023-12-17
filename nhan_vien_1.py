class NhanVien:
    cnt = 0

    def __init__(self) -> None:
        pass

    def __init__(self, name, gender, dob, addr, tax_code, contract_day):
        NhanVien.cnt += 1
        self.__id = f'SV{NhanVien.cnt:05d}'
        self.__name = name
        self.__gender = gender
        self.__dob = self.day_std(dob)
        self.__addr = addr
        self.__tax_code = tax_code
        self.__contract_day = self.day_std(contract_day)

    def get_id(self):
        return self.__id

    def day_std(self, s):
        if s[1] == '/':
            s = '0' + s
        if s[4] == '/':
            s = s[0:3] + '0' + s[3:]
        return s

    def get_day(self):
        arr = self.__dob.split('/')
        arr = arr[::-1]
        return ''.join(arr)

    def __str__(self):
        return f'{self.__id} {self.__name} {self.__gender} {self.__dob} {self.__addr} {self.__tax_code} {self.__contract_day}'

if __name__ == '__main__':
    t = int(input())
    a = []
    while t:
        nv = NhanVien(input(), input(), input(), input(), input(), input())
        a.append(nv)
        t -= 1
    a.sort(key= lambda x :(x.get_day(), x.get_id()))
    for x in a:
        print(x)
