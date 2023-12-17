if __name__ == '__main__':
    t = int(input())
    while t:
        n, m = map(int, input().split())
        a = list(map(int, input().split()))
        maxx = max(a)
        for i in range(n):
            if a[i] == maxx:
                a.insert(i, m)
                break
        
        for x in a:
            if x < 0:
                print(x, end=' ')
            
        for x in a:
            if x >= 0 :
                print(x, end=' ')
        print()
        t -= 1
