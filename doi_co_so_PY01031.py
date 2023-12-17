def conv(num, base):
    s = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ans = ''
    while num != 0:
        ans += s[num%base]
        num //= base
    return ans[::-1]

if __name__ == '__main__':
    t = int(input())
    while t:
        num, base = map(int, input().split())
        print(conv(num, base))
        t -= 1