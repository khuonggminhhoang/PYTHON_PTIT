if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        lst = []
        for _ in range(n):
            a, b = map(int, input().split())
            lst.append([a, b])

        lst.sort(key= lambda x : x[1])    
        cnt = 1
        point = lst[0][1]
        for x in lst:
            if x[0] >= point:
                cnt += 1
                point = x[1]
        print(cnt)

        t -= 1