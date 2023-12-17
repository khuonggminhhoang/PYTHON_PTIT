class Tram:
    cnt = 0
    
    def __init__(self, name, start, finish, amount):
        Tram.cnt += 1
        self.__id = f'T{Tram.cnt:02d}'
        self.__name = name
        self.__start = start
        self.__finish = finish
        self.__amount = amount
        self.time = self.convi_time(self.__finish) - self.convi_time(self.__start)

    def get_name(self):
        return self.__name

    def convi_time(self, time):
        return int(time[:2]) * 60 + int(time[3:])

    def set_time(self, start, finish):
        self.time += self.convi_time(finish) - self.convi_time(start)

    def set_amount(self, amount):
        self.__amount += amount

    def avg(self):
        time = self.time/60
        return self.__amount/ time

    def __str__(self):
        return f'{self.__id} {self.__name} {round(self.avg() * 100)/100:.2f}'

if __name__ == '__main__':
    t = int(input())
    dct = dict()
    while t:
        name = input()
        start = input()
        finish = input()
        amount = int(input())
        ok = 0
        for x in dct.keys():
            if x.get_name() == name:
                ok = 1
                x.set_amount(amount)
                x.set_time(start, finish)
                break
        if ok == 0 :
            dct[Tram(name, start, finish, amount)] = 1
        t -= 1
    
    for x in dct:
        print(x)