if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    tar = int(input())
    ans1 , ans2 = 0, 0
    for x in a:
        if( x < tar):
            ans1 += 1
        elif( x > tar):
            ans2 += 1
    print(ans1, ans2, sep = '\n')