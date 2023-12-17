def function1(a, cnt):
    for x in a:
        if cnt[x] != 0:
            print(x,cnt[x])
            cnt[x] = 0
    print()

def function2(a, cnt):
    left = min(a)
    right = max(a)
    for i in range(left, right + 1):
        if cnt[i] !=0:
            print(i, cnt[i])
    print()

def function3(a, cnt):
    max_ = max(cnt)
    for x in a:
        if cnt[x] == max_:
            ans = x
    return ans

def function4(a, cnt):
    min_ = 10**18
    for x in a:
        min_ = min(min_, cnt[x])

    for x in a:
        if cnt[x] == min_:
            return x


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    cnt = [0] * 1001
    for x in a:
        cnt[x] += 1
    
    function1(a, cnt[:])
    function2(a, cnt[:])
    a.sort()
    print(function3(a,cnt.copy()))
    print(function4(a,cnt.copy()))
    