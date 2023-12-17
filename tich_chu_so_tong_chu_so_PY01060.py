if __name__ == '__main__':
    t= int(input())
    while t:
        s = input()
        ans1, ans2 = 1, 0
        for i in range(len(s)):
            if i % 2 == 1:
                ans2 += int(s[i])
            elif s[i] != '0':
                ans1 *= int(s[i])
        print(ans1, ans2)
        t -= 1