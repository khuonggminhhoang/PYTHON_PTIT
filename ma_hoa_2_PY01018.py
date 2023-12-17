def encode(s, k):
    ans = ''
    for i in range(len(s)):
        ans += P[(P.find(s[i]) + k)%28]
    return ans[::-1]

if __name__ == '__main__':
    P = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
    while True:
        a = input().split()
        k = int(a[0])
        if k == 0:
            break
        s = a[1]
        print(encode(s,k))
        
