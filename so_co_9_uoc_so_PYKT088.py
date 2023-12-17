from math import *

def is_prime(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return n > 1

def solve(n):
    lst = []
    for i in range(2, isqrt(n) + 1):
        if is_prime(i):
            lst += [i]
    return lst

def calc_8(n):
    tmp = [2, 3, 5, 7, 11, 13] # số lớn nhất là 10^9 nên căn bậc 1/8 chỉ tới 13
    cnt = 0
    for i in range(2, int(n ** (1/8)) + 1):
        if i in tmp:
            cnt += 1
    return cnt

if __name__ == '__main__':
    n = int(input())
    lst = solve(n)
    ans = 0
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if lst[i] * lst[j] <= isqrt(n):
                ans += 1
    ans += calc_8(n)
    print(ans)
