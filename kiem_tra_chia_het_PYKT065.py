if __name__ == '__main__':
    while True:
        inp = list(map(int, input().split()))
        if inp[0] == -1: break
        l = inp[0]
        r = inp[1]
        n = int(input())
        cnt = 0
        for i in range(l, r + 1):
            check = False
            for k in range(2, n + 1):
                if i % k == 0:
                    check = True
                    break
            if not check: cnt += 1 
        print(cnt)
