if __name__ == '__main__':
    t = int(input())
    while t:
        s = input()
        flag = False
        ans1, ans2 = 0, 1
        for i in range(len(s)):
            if i % 2 == 0:
                ans1 += int(s[i])
            elif s[i] != '0':
                flag = True
                ans2 *= int(s[i])
        print(ans1, end=' ')
        print(ans2 if flag else 0)
        t -= 1