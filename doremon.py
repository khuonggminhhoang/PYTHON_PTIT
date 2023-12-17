n, m = map(int, input().split())
if n%2 == 0 :
    tmp = n//2
else : tmp = n//2 + 1
minStep = ((tmp) + m - 1) // m * m
if(minStep <= n): print(minStep)
else : print(-1)
