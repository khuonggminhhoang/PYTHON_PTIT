class LichThi:
    cnt = 0
    dct = {}

    def __init__(self, idSub, date, time, group):
        LichThi.cnt += 1
        self.id = f'T{LichThi.cnt:03d}'
        self.idSub = idSub
        self.date = date
        self.time = time
        self.group = group

    def getId(self):
        return self.id
    
    def convDate(self):
        arr = self.date.split('/')
        arr = arr[::-1]
        return int(''.join(arr))

    def convTime(self):
        arr = self.time.split(':')
        return int(arr[0]) * 60 + int(arr[-1])
    
    def __str__(self):
        return f'{self.id} {self.idSub} {LichThi.dct[self.idSub]} {self.date} {self.time} {self.group}'

if __name__ == '__main__':
    n, m = map(int, input().split())
    for _ in range(n):
        key = input()
        LichThi.dct[key] = input()

    a = []
    for _ in range(m):
        lst = input().split()
        a.append(LichThi(lst[0], lst[1], lst[2], lst[3]))

    a.sort(key = lambda x : (x.convDate(), x.convTime(), x.getId()))

    for x in a:
        print(x)
    

