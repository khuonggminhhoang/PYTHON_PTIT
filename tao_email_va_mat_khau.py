if __name__ == '__main__':
    t = int(input())
    while t:
        a = input().lower().split()
        ans = a[-2]
        for i in range(len(a) - 2):
            ans += a[i][0]
        ans += '@xyz.edu.vn'
        password = ''
        arr = a[-1].split('/')
        for x in arr:
            password += str(int(x))
        print(ans)
        print(password)
        t -= 1