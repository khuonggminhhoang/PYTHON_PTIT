class Invoice:
    cnt = 0
    
    def __init__(self, name, oldest, lastest):
        Invoice.cnt += 1
        self.__id = f'KH{Invoice.cnt:02d}'
        self.__name = name
        self.__oldest = oldest
        self.__lastest = lastest

    def unit_price(self):
        tmp = self.__lastest - self.__oldest
        if tmp <= 50: return tmp * 100
        elif tmp <= 100: return 50 * 100 + (tmp - 50) * 150
        else: return 50 * 100 + 50 * 150 + (tmp - 100) * 200

    def surcharge(self):
        tmp = self.__lastest - self.__oldest
        if tmp <= 50: return 0.02
        elif tmp <= 100: return 0.03
        else: return 0.05

    def total(self):
        return self.unit_price() *(1 + self.surcharge())

    def __str__(self):
        return f'{self.__id} {self.__name} {round(self.total())}'

if __name__ == '__main__':
    t = int(input())
    a = []
    for _ in range(t):
        a.append(Invoice(input(), int(input()), int(input())))
    a.sort(key = lambda x : -x.total())
    for x in a:
        print(x)