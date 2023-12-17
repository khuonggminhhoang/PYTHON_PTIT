class SinhVien:
    def __init__(self, id, name, classs, email):
        self.__id = id
        self.__name = self.name_std(name)
        self.__classs = classs
        self.__email = email
    
    def name_std(self, s):
        arr = s.strip().title().split()
        return ' '.join(arr)

    def get_id(self):
        return self.__id

    def get_class(self):
        return self.__classs
    
    def __str__(self):
        return f'{self.__id} {self.__name} {self.__classs} {self.__email}'

if __name__ == '__main__':
    t = int(input())
    a = []
    for _ in range(t):
        a.append(SinhVien(input(), input(), input(), input()))

    t = int(input())
    for _ in range(t):
        year = input()
        print(f'DANH SACH SINH VIEN KHOA {year} :')
        for x in a:
            if x.get_id()[0:4] == year:
                print(x)
