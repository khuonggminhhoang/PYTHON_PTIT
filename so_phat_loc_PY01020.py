def check(n):
    tmp1 = n%10
    tmp2 = (n//10)%10
    if (tmp1 == 6 and tmp2 == 8): 
        return True
    return False

if __name__ == '__main__':
    t = int(input())
    while t != 0:
        n = int(input())
        print('YES' if check(n) else 'NO')
        t-=1

# 3
# 1539786
# 1234789
# 8686