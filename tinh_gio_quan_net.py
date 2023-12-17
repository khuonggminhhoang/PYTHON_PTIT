class Gamer:
    def __init__(self, username, password, name, in_hour, out_hour):
        self.__username = username
        self.__password = password
        self.__name = name
        self.__in_hour = in_hour
        self.__out_hour = out_hour

    def convi_time(self, time):
        return int(time[0:2]) * 60  + int(time[3:])
    
    def get_time(self):
        return self.convi_time(self.__out_hour) - self.convi_time(self.__in_hour)

    def get_username(self):
        return self.__username
    
    def __str__(self):
        return f'{self.__username} {self.__password} {self.__name} {self.__in_hour} {self.__out_hour}'

if __name__ == '__main__':
    t = int(input())
    a = []
    while t:
        x = Gamer(input(), input(), input(), input(), input())
        a += [x]
        t -= 1
    a.sort(key= lambda x : (-x.get_time(), x.get_username()))
    for x in a:
        print(x)