def check(n):
    if len(n) == 1:
        return int(n)  % 4 == 0
    n = n[- 2:]
    return int(n) % 4 == 0

if __name__ == '__main__':
    s = input()
    print('YES' if check(s) else 'NO')