from math import log2

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        lst = list(map(int, input().split()))
        ans = 0
        for i in range(1, n):
            maxx = max(lst[i], lst[i - 1]) - 1
            minx = min(lst[i], lst[i - 1])
            tmp = int(maxx//minx)
            if tmp != 0:
                ans += int(log2(tmp))
        print(ans)
'''
6
4
4 2 10 1
2
1 3
2
6 1
3
1 4 2
5
1 2 3 4 3
12
4 31 25 50 30 20 34 46 42 16 15 16

'''