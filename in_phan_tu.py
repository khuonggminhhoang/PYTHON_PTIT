if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(2, n, 2):
        if a[i] % 2 == 0:
            flag = True
            print(a[i],end=' ')
    if not flag: print("NONE")