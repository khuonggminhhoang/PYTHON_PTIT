def solve(s, n):
    while n :
        print(s, end='')
        n -= 1

if __name__ == '__main__':
    t = int(input())
    while t:
        s = input()
        for i in range(0, len(s), 2):
            solve(s[i], int(s[i + 1]))
        print()
        t -= 1