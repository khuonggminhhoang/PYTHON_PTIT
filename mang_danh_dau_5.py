if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    cnt = [0] * 1000001
    maxx = -10**18
    for x in a :
        cnt[x] += 1 
        maxx = max(maxx, cnt[x])
    
    for x in a:
        if cnt[x] == maxx:
            print(x, cnt[x])
            break