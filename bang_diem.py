class HocSinh:
    cnt = 0
    
    def __init__(self, name, m1, m2, m3, m4, m5, m6, m7, m8, m9, m10):
        HocSinh.cnt += 1
        self.__id = f'HS{HocSinh.cnt:02d}'
        self.__name = name
        self.__m1 = m1
        self.__m2 = m2
        self.__m3 = m3
        self.__m4 = m4
        self.__m5 = m5
        self.__m6 = m6
        self.__m7 = m7
        self.__m8 = m8
        self.__m9 = m9
        self.__m10 = m10

    def get_id(self):
        return self.__id

    def avg(self):
        return (self.__m1 + self.__m2 + self.__m3 + self.__m4 + self.__m5 + self.__m6 + self.__m7 + self.__m8 + self.__m9 + self.__m10)/10

    def classify(self):
        tmp = self.avg()
        if tmp >= 9: return 'XUAT SAC'
        elif tmp >= 8: return 'GIOI'
        elif tmp >= 7: return 'KHA'
        elif tmp >=5 : return 'TB'
        else : return 'YEU'
    
    def __str__(self):
        return f'{self.__id} {self.__name} {self.avg()} {self.classify()}'

if __name__ == '__main__':
    t = int(input())
    arr = []
    while t:
        name = input()
        m = list(map(float, input().split()))
        arr.append(HocSinh(name, m[0], m[1], m[2], m[3], m[4], m[5], m[6], m[7], m[8], m[9]))
        t -= 1

    arr.sort(key = lambda x : (-x.avg(), x.get_id()))
    for x in arr:
        print(x)