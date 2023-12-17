if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        s = input().split()
        cnt = 0 
        for x in s:
            if cnt + len(x) <= 100:
                print(x, end=' ')
                cnt += len(x) + 1
            else:
                break
        print()
