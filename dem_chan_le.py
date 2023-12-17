if __name__ == '__main__':
    cntOdd = 0
    cntEven = 0
    sumOdd, sumEven = 0, 0
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        if(a[i] % 2 == 0):
            cntEven += 1
            sumEven += a[i]
        else:
            cntOdd += 1
            sumOdd += a[i]
        
    print(cntEven)
    print(cntOdd)
    print(sumEven)
    print(sumOdd)