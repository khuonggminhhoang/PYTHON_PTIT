class Gamer:
    def __init__(self, id, name, start, end):
        self.__id = id
        self.__name = name
        self.__start = start
        self.__end = end

    def convi_time(self, time):
        return int(time[:2]) * 60 + int(time[3:])

    def convt_time(self, time):
        return f'{time//60} gio {time % 60} phut'

    def time(self):
        start = self.convi_time(self.__start)
        end = self.convi_time(self.__end)
        return end - start

    def __str__(self):
        return f'{self.__id} {self.__name} {self.convt_time(self.time())}'

if __name__ == '__main__':
    t = int(input())
    a = []
    while t :
        a.append(Gamer(input(), input(), input(), input()))
        t -=1
    a.sort(key = lambda x : -x.time())
    for x in a:
        print(x)

