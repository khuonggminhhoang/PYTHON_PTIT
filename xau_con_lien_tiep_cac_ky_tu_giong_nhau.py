if __name__ == '__main__':
    s = input() + '#'
    tmp = s[0]
    ans = s[0]
    res = 1
    cnt = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            cnt +=1
            tmp += s[i]
        else:
            if cnt > res:
                ans = tmp
                res = cnt
            elif cnt == res:
                if tmp > ans:
                    ans = tmp
            cnt = 1
            tmp = s[i]
    print(ans)