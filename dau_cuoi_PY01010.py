def check(n):
    num1 = 0
    cnt = 0
    for i in n:
        cnt+=1
        if cnt < 3:
            num1 = num1 * 10 + int(i)
    num2 = int(n)%100
    return num1 == num2

if __name__ == '__main__':
    t = int(input())
    while t :
        n = input()
        print('YES' if check(n) else 'NO')
        t-=1
