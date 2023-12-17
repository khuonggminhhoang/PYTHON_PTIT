if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    cnt = [0] * 1000001
    for x in a:
        cnt[x] += 1
    left = min(a)
    right = max(a)
    for i in range(left, right +1):
        if cnt[i] != 0:
            print(i, cnt[i])