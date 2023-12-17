from datetime import datetime

class HoaDon:
    cnt = 0
    
    def __init__(self, name, room, dateIn, dateOut, service):
        HoaDon.cnt += 1
        self.__id = f'KH{HoaDon.cnt:02d}'
        self.__name = name
        self.__room = room
        self.__dateIn = dateIn
        self.__dateOut = dateOut
        self.__service = service

    def invoice(self):
        tmp = self.__room//100
        if tmp == 1: return 25
        elif tmp == 2: return 34
        elif tmp == 3: return 50
        return 80

    def daily(self):
        arrIn = list(map(int, self.__dateIn.split('/')))
        arrOut = list(map(int, self.__dateOut.split('/')))
        dayIn = datetime(arrIn[2], arrIn[1], arrIn[0])
        dayOut = datetime(arrOut[2], arrOut[1], arrOut[0])
        return (dayOut - dayIn).days + 1
    
    def total(self):
        return self.daily() * self.invoice() + self.__service

    def __str__(self):
        return f'{self.__id} {self.__name} {self.__room} {self.daily()} {self.total()}'

if __name__ == '__main__':
    t = int(input())
    arr = []
    for _ in range(t):
        arr.append(HoaDon(input().strip(), int(input()), input(), input(), int(input())))
    
    arr.sort(key=lambda x : -x.total())    
    for x in arr:
        print(x)
    s = str(s)
    s.capitalize()



    