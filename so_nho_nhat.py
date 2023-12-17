if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    min = min(a)
    ans = a.count(min)
    print(ans)