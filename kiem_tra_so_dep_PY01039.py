def diff(n):
    a = set(n)
    return len(a)

def check(n):
    for i in range(len(n)-2):
        if n[i] != n[i + 2]:
            return False
    return True

if __name__ == '__main__':
    t = int(input())
    while t:
        n = input()
        if check(n) and diff(n) == 2:
            print('YES')
        else:
            print('NO')
        t -= 1