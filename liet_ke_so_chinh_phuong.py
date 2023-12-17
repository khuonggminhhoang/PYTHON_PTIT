import math

n = int(input())
for i in range(1, math.isqrt(n) + 1, 1):
    print(i**2, end= " ")
