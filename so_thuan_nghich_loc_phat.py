def stn(n):
    sum = 0
    tmp = n
    while tmp != 0:
        sum = sum*10 + tmp%10
        tmp //= 10
    return sum == n

def check(n):
    sum = 0
    cnt6 = 0
    while n!=0:
        if n%10 == 6: cnt6 +=1
        sum += n%10
        n//=10
    if cnt6 >=1 and sum%10 == 8: return True
    return False

if __name__ == '__main__':
    a, b = map(int, input().split())
    for i in range(a,b+1):
        if stn(i) and check(i):
            print(i, end=' ')