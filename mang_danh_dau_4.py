if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    cnt = [0] * 1000001
    maxx = -10**18
    for x in a:
        cnt[x] +=1
        maxx = max(maxx, cnt[x])
    
    left = min(a)
    right = max(a)

    for i in range(left, right + 1):
        if cnt[i] == maxx:
            print(i, cnt[i])
            break
        