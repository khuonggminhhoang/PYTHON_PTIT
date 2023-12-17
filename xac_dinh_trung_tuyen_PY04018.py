class GiangVien:
    cnt = 0

    def __init__(self, ten, ma_xet, diem_tin, diem_chuyen_mon ):
        GiangVien.cnt += 1
        self.__id = f'GV{GiangVien.cnt:02d}'        
        self.__ten = ten
        self.__ma_xet = ma_xet
        self.__diem_tin = diem_tin
        self.__diem_chuyen_mon = diem_chuyen_mon

    def get_uu_tien(self):
        tmp = self.__ma_xet[1:]
        if tmp == '1': return 2.0
        elif tmp == '2': return 1.5
        elif tmp == '3': return 1.0
        return 0.0
    
    def get_mon(self):
        tmp = self.__ma_xet[0]
        if tmp == 'A': return 'TOAN'
        elif tmp == 'B': return 'LY'
        else : return 'HOA'
    
    def get_tong(self):
        return self.__diem_tin * 2 + self.__diem_chuyen_mon + self.get_uu_tien()
    
    def __str__(self):
        tmp = 'TRUNG TUYEN' if self.get_tong() >= 18 else 'LOAI'
        return f'{self.__id} {self.__ten} {self.get_mon()} {self.get_tong():.1f} {tmp}'
    
if __name__ == '__main__':
    t = int(input())
    lst = []
    while t:
        lst.append(GiangVien(input(), input(), float(input()), float(input())))
        t -= 1
    lst.sort(key= lambda x : -x.get_tong())
    for x in lst:
        print(x)
    