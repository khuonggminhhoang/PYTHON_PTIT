def conv(num, base):
    s = '0123456789ABCDEF'
    ans = ''
    while num != 0:
        ans += s[num%base]
        num //= base
    return ans[::-1]

if __name__ == '__main__':
    t = int(input())
    while t:    
        base = int(input())
        num = int(input(),2)
        print(conv(num, base))
        t-=1

# 2
# 8
# 10010100010010101
# 2
# 10010100010010101