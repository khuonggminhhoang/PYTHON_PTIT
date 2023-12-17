from sys import *
from math import *

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    ans = 0
    docung = maxsize
    for x in a:
        if docung <= 0:
            break
        ans += 1
        docung = min(docung, x)
    print(ans)
    