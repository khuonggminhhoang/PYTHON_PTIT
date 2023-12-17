def conv(s):
    a = [4, 2, 1]
    s = s[::-1]
    while len(s) % 3 != 0:
        s += '0'
    s = s[::-1]
    res = ''
    s = list(s)
    while len(s) != 0:
        tmp = s[(len(s) - 3) : len(s)]
        s[(len(s) - 3) : len(s)] = []
        ans = 0
        for i in range(3):
            if tmp[i] == '1':
                ans += a[i]
        res += str(ans)
    return res[::-1]

if __name__ == '__main__':
    s = input()
    print(int(conv(s)))