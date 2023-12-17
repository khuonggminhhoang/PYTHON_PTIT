if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    set = set()
    for x in a:
        if x not in set:
            print(x, end=' ')
            set.add(x)
        
