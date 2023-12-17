if __name__ == '__main__':
    t = int(input())
    while t:
        a, b = map(int, input().split())
        arr = [0] * 10
        
        for i in range(a, b + 1):
            s = str(i)
            for c in s:
                arr[int(c)] += 1

        print(*arr)

        t -= 1