if __name__ == '__main__':
    n = int(input())
    a = list(map(int,input().split()))
    cnt = [0] * 1000001
    ans = 0
    for x in a:
        if(cnt[x] == 0):
            ans += 1
            cnt[x] += 1
    print(ans)