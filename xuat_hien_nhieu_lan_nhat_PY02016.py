if __name__ == '__main__':
    t = int(input())
    while t :
        n = int(input())
        a = list(map(int, input().split()))
        cnt = [0] * 1000001
        ans = 0
        for x in a:
            cnt[x] += 1
            ans = max(ans, cnt[x])
        flag = False
        for i in range(1000001):
            if cnt[i] == ans and ans > n//2:
                flag = True
                print(i)
                break
        if not flag:
            print('NO')
        t-= 1