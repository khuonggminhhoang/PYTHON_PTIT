from math import *

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    ans = 10**18
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            ans = min(ans, abs(a[i] - a[j]))
    print(ans)
