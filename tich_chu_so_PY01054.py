def mul_digit(s):
    ans = 1
    for x in s:
        if x != '0':
            ans *= int(x)
    return ans

if __name__ == '__main__':
    t = int(input())
    while t :
        s = input()
        print(mul_digit(s))
        t -= 1