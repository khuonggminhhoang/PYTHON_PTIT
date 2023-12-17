if __name__ == '__main__':
    t = int(input())
    while t:
        s = input()
        cnt = 1
        ans = []
        s = s + '_'
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                cnt += 1
            else:
                ans.append([cnt, s[i]])
                cnt = 1
        for x, y in ans:
            print(x, y, sep='', end='')
        print()
        t -= 1