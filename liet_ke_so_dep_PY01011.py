def stn(n):
    tmp = str(n)
    rev = tmp[::-1]
    return rev == tmp

def cntDigit(n):
    return len(str(n)) % 2 == 0

def check(n):
    s = str(n)
    for x in s:
        if x != '0' and x !='2' and x != '4' and x != '6' and x != '8':
            return False
    return True

def solve(n):
    if stn(n) and check(n) and cntDigit(n):
        return True
    return False

if __name__ == '__main__':
    t = int(input())
    lst = []
    for i in range(22, 10**6 + 1, 2):
            if solve(i):
                lst += [i]
    while t!=0:
        n = int(input())
        for x in lst:
            if x < n:
                print(x, end=' ')
            
        print()
        t-=1