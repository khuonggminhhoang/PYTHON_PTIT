if __name__ == '__main__':
    s = input()
    s += s[-1]
    cnt = 0
    tmp = s[0]
    res = 1
    ans = s[0]
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            cnt += 1
            tmp += s[i]
        else:
            if cnt > res:
                res = cnt
                ans = tmp
            elif cnt == res:
                if tmp > ans:
                    ans = tmp
            tmp = s[i]
            cnt = 0
    print(ans)