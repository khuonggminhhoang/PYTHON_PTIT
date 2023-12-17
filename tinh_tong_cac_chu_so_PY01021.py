if __name__ == '__main__':
    t = int(input())
    while t:
        s = input()
        ans = []
        num = 0
        for x in s:
            if x.isdigit():
                num += int(x)
            else:
                ans += [x]
        ans.sort()
        print(''.join(ans) + str(num))
        t -= 1