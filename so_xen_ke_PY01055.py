def cond1(s):
    return s[0] != s[1]

def cond2(s):
    for i in range(0, len(s) -3, 2):
        if s[i] != s[i + 2]:
            return False
    return True

if __name__ == '__main__':
    t = int(input())
    while t:
        s = input()
        print('YES' if (len(s) % 2 == 1) and cond1(s) and cond2(s) else 'NO')
        t -=1