def mul_digit(s):
    ans = 1
    for x in s:
        ans *= int(x)
    return ans

if __name__== '__main__':
    t = int(input())
    while t:
        n = int(input())
        a = input().split()
        a.sort(key = lambda x : (mul_digit(x), int(x)))
        for x in a:
            print(x, end=' ')
        print()
        t -= 1