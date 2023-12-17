if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        a = list(map(int, input().split()))
        a.sort()
        ans = 0
        for i in range(n-2):
            left, right = i+1, n-1
            while left < right:
                tmp = a[i] + a[left] + a[right]
                if not tmp:
                    ans += 1
                    left += 1
                elif tmp < 0:
                    left += 1
                else:
                    right -= 1
        print(ans)
        t -= 1