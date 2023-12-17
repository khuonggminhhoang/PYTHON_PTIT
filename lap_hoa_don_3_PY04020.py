class HoaDon:
    def __init__(self, id, name, qty, price, disc):
        self.__id = id
        self.__name = name
        self.__qty = qty
        self.__price = price
        self.__disc = disc

    def get_total(self):
        return self.__price * self.__qty - self.__disc

    def __str__(self):
        return f'{self.__id} {self.__name} {self.__qty} {self.__price} {self.__disc} {self.get_total()}'    

if __name__ == '__main__':
    t = int(input())
    lst = []
    for _ in range(t):
        lst.append(HoaDon(input(), input(), int(input()), int(input()), int(input())))
    lst.sort(key= lambda x : -x.get_total())
    print(*lst, sep='\n')

    