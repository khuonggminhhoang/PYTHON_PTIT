def check(s):
    ans = set(s)
    for x in ans:
        if x != '0' and x != '1' and x != '2':
            return False
    return True

if __name__ == '__main__':
    t = int(input())
    while t:
        s = input()
        print('YES' if check(s) else 'NO')
        t -= 1