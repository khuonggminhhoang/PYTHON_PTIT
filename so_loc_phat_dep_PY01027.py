def check(s):
    for x in s:
        if x != '6' and x != '8':
            return False
    s = s.replace('688', '')
    s = s.replace('68', '')
    s = s.replace('6', '')
    if len(s) != 0:
        return False
    return True

if __name__ == '__main__':
    s = input()
    print('YES' if check(s) else 'NO')
    