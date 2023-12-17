class Exam:
    cnt = 0
    def __init__(self, date, time, room):
        Exam.cnt += 1
        self.__id = f'C{Exam.cnt:03d}'
        self.__date = date
        self.__time = time
        self.__room = room

    def get_date(self):
        tmp = self.__date.split("/")
        tmp = tmp[::-1]
        ans = ''
        for i in tmp:
            ans += i
        return int(ans)
        
    def get_time(self):
        tmp = self.__time.split(":")
        return int(tmp[0]) * 60 + int(tmp[-1])
        
    def get_id(self):
        return self.__id
    
    def __str__(self):
        return '{} {} {} {}'.format(self.__id, self.__date, self.__time, self.__room)
        
if __name__ == '__main__':
    f = open('CATHI.in', 'rt')
    t = int(f.readline())
    arr = []
    while(t):
        date = f.readline().strip()
        time = f.readline().strip()
        room = f.readline().strip()
        arr.append(Exam(date, time, room))
        t -= 1
    arr.sort(key= lambda x : (x.get_date(), x.get_time(), x.get_id()))
    for x in arr:
        print(x)
    f.close()