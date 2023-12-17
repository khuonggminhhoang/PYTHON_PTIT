from sys import stdin

if __name__ == '__main__':
    n = int(stdin.readline())
    a = []
    ans = []
    for line in stdin:
        a += list(map(int, line.split()))
    min_ = min(a)
    max_ = max(a)
    lst = [0] * (max_ + 1)
    for x in a:
        lst[x] = 1
    for i in range(1, max_ + 1):
        if lst[i] == 0:
            ans += [i]
    if ans == []:
        print('Excellent!')
    else:
        for x in ans:
            print(x)
