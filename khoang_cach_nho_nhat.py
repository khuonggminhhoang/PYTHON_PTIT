from sys import *

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = maxsize
    for i in range(n-1):
        ans = min(ans, a[i+1] - a[i])
    print(ans)
    
