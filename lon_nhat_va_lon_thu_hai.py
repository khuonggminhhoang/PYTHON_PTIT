if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    max1 = max(a)
    a.remove(max1)
    max2 = max(a)
    print(max1, max2 )