def check(a,  b, n):
    for i in range(n):
        if a[i] > b[i]:
            return False
    return True

if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        a.sort()
        b.sort()
        print('YES' if check(a, b, n) else 'NO')
        t -=1 