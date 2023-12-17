a = [[10, 12, 14, 20],
     [10, 11, 13, 16],
     [9, 10, 12, 14],
     [8, 9, 11, 13]]

class PhongBan:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name
    
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

class NhanVien:
    def __init__(self, id, name, sal, work_day):
        self.__id = id
        self.__name = name
        self.__sal = sal
        self.__work_day = work_day
    
    def set_room(self, room):
        self.__room = room

    def get_id_room(self):
        return self.__id[3:]

    def get_row(self):
        tmp = self.__id[0]
        return ord(tmp) - ord('A')

    def get_col(self):
        tmp = int(self.__id[1:3])
        if 1<= tmp <= 3: return 0
        elif tmp <= 8: return 1
        elif tmp <= 15: return 2
        else: return 3

    def get_coef(self):
        return a[self.get_row()][self.get_col()]

    def get_total(self):
        return self.__sal * self.__work_day * self.get_coef() * 1000

    def __str__(self):
        return f'{self.__id} {self.__name} {self.__room.get_name()} {self.get_total()}'

if __name__ == '__main__':
    t = int(input())
    arr = []
    for _ in range(t):
        s = input()
        arr.append(PhongBan(s[0:2], s[3:]))

    t = int(input())
    for _ in range(t):
        nv = NhanVien(input(), input(), int(input()), int(input()))
        for x in arr:
            if x.get_id() == nv.get_id_room():
                nv.set_room(x)
                print(nv)
                break