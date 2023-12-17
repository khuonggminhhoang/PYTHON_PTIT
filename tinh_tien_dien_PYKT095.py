class KhachHang:
    cnt = 0

    def __init__(self, name, type, first, second):
        KhachHang.cnt += 1
        self.__id = f'KH{KhachHang.cnt:02d}'
        self.__type = type
        self.__name = self.name_std(name)
        self.__first = first
        self.__second = second

    def get_num_elec(self):
        return self.__second - self.__first

    def name_std(self, name):
        arr = name.strip().title().split()
        return ' '.join(arr)

    # định mức
    def get_quota(self):
        if self.__type == 'A': return 100
        elif self.__type == 'B': return 500
        else: return 200

    def get_money_quota(self):
        tmp = self.get_num_elec()
        return tmp * 450 if tmp < self.get_quota() else self.get_quota() * 450

    def get_money_over_quota(self):
        tmp = self.get_num_elec() - self.get_quota()
        return tmp * 1000 if self.get_num_elec() > self.get_quota() else 0
    
    def get_vat(self):
        return self.get_money_over_quota()//20
    
    def get_total(self):
        return self.get_money_quota() + self.get_money_over_quota() + self.get_vat()

    def __str__(self) -> str:
        return f'{self.__id} {self.__name} { self.get_money_quota()} {self.get_money_over_quota()} {self.get_vat()} {self.get_total()}'

if __name__ == '__main__':
    t = int(input())
    arr = []
    for _ in range(t):
        name = input()
        s = input().split()
        kh = KhachHang(name, s[0], int(s[1]), int(s[2]))
        arr.append(kh)

    arr.sort(key = lambda x : -x.get_total())
    print(*arr, sep='\n')