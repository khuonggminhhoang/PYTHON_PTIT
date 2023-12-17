class SinhVien:
    def __init__(self, name, email, phone, m1, m2, m3):
        self.__name = name
        self.__email = email
        self.__phone = phone
        self.__m1 = m1
        self.__m2 = m2
        self.__m3 = m3
    
    def get_total(self):
        return self.__m1 + self.__m2 + self.__m3

    def __str__(self):
        if self.get_total() == int(self.get_total()):
            tmp = str(int(self.get_total()))
        return f'{self.__name}\n{self.__email}\n{self.__phone}\n{tmp}'

if __name__ == '__main__':
    inp = open('DiemThi.txt', 'rt')
    out = open('TrungTuyen.txt', 'wt')

    arr = []
    lst = inp.read().split('\n')
    for i in range(0, len(lst), 4):
        m = list(map(float, lst[i + 3].split()))
        sv = SinhVien(lst[i], lst[i + 1], lst[i + 2], m[0], m[1], m[2])
        if sv.get_total() >= 27:
            arr.append(sv)
    arr.sort(key = lambda x : -x.get_total())
    for x in arr:
        out.write(x.__str__() + '\n')
    inp.close()
    out.close()