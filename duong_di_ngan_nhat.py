import math
d1, d2, d3 = map(int, input().split())
minVal = 1e8 + 1
a = 2 * (d1 + d2)
b = 2 * (d1 + d3)
c = 2 * (d2 + d3)
d = d1 + d2 + d3
ans = min(a,b,c,d)
print(ans)
