def conv(n, coef):
    a = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    res =''
    if n==0: return '0'
    while n!=0:
        res += a[n%coef]
        n //= coef
    return res[::-1]
    
if __name__ == '__main__':
    t = int(input())
    while t:
        n, coef = map(int,input().split())
        print(conv(n,coef))
        t -= 1