if __name__ == '__main__':
    n = int(input())
    lst = list(map(int, input().split()))
    min_ = int(1e9)
    for x in lst:
        tmp = 0
        for y in lst:   
            tmp += abs(x - y)
        
        if tmp < min_:
            min_ = tmp
            key = x
    
    print(min_, key)