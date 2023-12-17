class Nguoi:
    def __init__(self, id, name, dob, addr):
        self._id = id
        self._name = self.name_std(name)
        self._dob = self.day_std(dob)
        self._addr = addr

    def name_std(self, s):
        arr = s.strip().title().split()
        return ' '.join(arr)

    def day_std(self, s):
        if s[1] == '/':
            s = '0' + s
        if s[4] == '/':
            s = s[:3] + '0' + s[3:]
        return s
    
    def __str__(self):
        return f'{self._id} {self._name} {self._dob} {self._addr}'

class SinhVien(Nguoi):
    def __init__(self, id, name, dob, addr, classs, gpa):
        Nguoi.__init__(self, id, name, dob, addr)
        self.__classs = classs
        self.__gpa = gpa

    def __str__(self):
        return super().__str__() + ' ' + f'{self.__classs} {self.__gpa:.2f}'

class GiaoVien(Nguoi):
    def __init__(self, id, name, dob, addr, spec, sal):
        Nguoi.__init__(self, id, name, dob, addr)
        self.__spec = spec
        self.__sal = sal

    def __str__(self):
        return super().__str__() + ' ' + f'{self.__spec} {self.__sal}'

if __name__ == '__main__':
    t = int(input())
    arr_sv = []
    arr_gv = []
    for _ in range(t):
        id = input()
        name = input()
        dob = input()
        addr = input()
        if id[:2] == 'SV':
            arr_sv.append(SinhVien(id, name, dob, addr, input(), float(input())))
        else:
            arr_gv.append(GiaoVien(id, name, dob, addr, input(), input()))
    print('DANH SACH GIAO VIEN :')
    for x in arr_gv:
        print(x)
    print('DANH SACH SINH VIEN :')
    for x in arr_sv:
        print(x)