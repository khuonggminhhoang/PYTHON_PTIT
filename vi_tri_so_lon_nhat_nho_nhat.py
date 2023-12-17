if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    min = min(a)
    max = max(a)
    flag = True
    for i in range(n):
        if a[i] == min:
            minIdx = i
        if flag and a[i] == max:
            flag = False
            maxIdx = i
    print(minIdx, maxIdx)
