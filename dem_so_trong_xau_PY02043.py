if __name__ == '__main__':
    t = int(input())
    while t:
        s = input()
        sub = input()
        ans = 0
        while sub in s:
            i = s.index(sub)
            s = s[:i] + s[(i + len(sub)):]
            ans += 1
        print(ans)
        t -= 1