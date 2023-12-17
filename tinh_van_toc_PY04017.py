class CuaRo:
    def __init__(self, name, addr, finish):
        ans = []
        ans += [x[0] for x in addr.split()]
        ans += [x[0] for x in name.split()]

        self.id = ''.join(ans)
        self.name = name
        self.addr = addr
        self.finish = finish
    
    def time(self):
        arr = self.finish.split(':')
        return (int(arr[0]) - 6) + (int(arr[-1]))/60

    def speed(self):
        return 120/self.time()
    
    def __str__(self):
        return f'{self.id} {self.name} {self.addr} {round(self.speed())} Km/h'

if __name__ == '__main__':
    t = int(input())
    a = []
    while t:
        a.append(CuaRo(input(), input(), input()))
        t -= 1
    a.sort(key= lambda x : -x.speed())
    for x in a:
        print(x)