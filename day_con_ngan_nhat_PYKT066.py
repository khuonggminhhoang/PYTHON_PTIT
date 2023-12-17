from math import *

if __name__ == '__main__':
    t = int(input())
    while t :
        ans = 10**9 + 1
        n, k_ = map(int, input().split())
        a = list(map(int, input().split()))
        for i in range(n):
            for j in range(i , n):
                tmp = gcd(a[i], a[j])
                for k in range(i, j + 1):
                    tmp = gcd(tmp, a[k])
                if tmp == k_:
                    ans = min(ans, j - i + 1)
        ans = (ans if ans != 10**9 + 1 else -1)
        print(ans)
        

        t -= 1
