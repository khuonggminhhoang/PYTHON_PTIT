def check(s):
    n = 0
    lt = 1
    for x in s[::-1]:
        n += int(x) * lt
        lt *= 2
        n %= 5
        lt %= 5
    return n % 5 == 0

if __name__ == '__main__':
    s = input()
    print('YES' if check(s) else 'NO')
