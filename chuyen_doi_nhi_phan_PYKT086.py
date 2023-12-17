def conv(num, base):
    s = '0123456789ABCDEF'
    ans = ''
    while num != 0:
        ans += s[num%base]
        num //= base
    return ans[::-1]

if __name__ == '__main__':
    f = open('DATA.in', 'rt')
    t = int(f.readline())
    while t:
        base = int(f.readline())
        num = int(f.readline(), 2)
        print(conv(num, base))
        t -= 1
    