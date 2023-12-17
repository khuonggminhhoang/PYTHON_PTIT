class SinhVien:
    cnt = 0
    
    def __init__(self) :
        pass

    def __init__(self, name, classs, dob, gpa):
        SinhVien.cnt += 1
        self.__id = f'SV{SinhVien.cnt:03d}'    
        self.__name = self.namestd(name)
        self.__classs = classs
        self.__dob = self.daystd(dob)
        self.__gpa = gpa

    def daystd(self, s) -> str:
        if s[1] == '/':
            s = '0' + s
        if s[4] == '/':
            s = s[0:3] + '0' + s[3:]
        return s
    
    def namestd(self, s) -> str:
        arr = s.strip().title().split()
        return ' '.join(arr)
    
    def getGpa(self):
        return self.__gpa

    def getId(self):
        return self.__id

    def __str__(self) -> str:
        return f'{self.__id} {self.__name} {self.__classs} {self.__dob} {self.__gpa:.2f}'

if __name__ == '__main__':
    t = int(input())
    arr = []
    while t:
        sv = SinhVien(input(), input(), input(), float(input()))
        arr.append(sv)
        t -= 1
    arr.sort(key = lambda x : (- x.getGpa(), x.getId()))
    for x in arr:
        print(x)

