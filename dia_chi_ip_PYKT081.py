def check(s):
    a = s.split('.')
    if len(a) != 4: return False
    for x in a:
        if not x.isnumeric(): return False
        if int(x) < 0 or int(x) > 255:
            return False
    return True

if __name__ == '__main__':
    t = int(input())
    while t:
        s = input()
        print('YES' if check(s) else 'NO')
        
        t -= 1