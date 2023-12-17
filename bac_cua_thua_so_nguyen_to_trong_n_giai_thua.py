import math

def solve(n,p):
    cnt = 0
    ans = 0
    for x in range(p, n+1,p):
        if x%p ==0:
            while x%p == 0:
                cnt+=1
                x//=p
        ans += cnt
    return cnt

if __name__ == '__main__':
    n,p = map(int, input().split())
    print(solve(n,p))