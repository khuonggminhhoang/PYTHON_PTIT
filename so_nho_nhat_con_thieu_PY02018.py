if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    id = 1
    flag = True
    for i in range(1, n + 1):
        if i not in a:
            print(i)
            flag = False
            break
    
    if flag :
        print(n + 1)