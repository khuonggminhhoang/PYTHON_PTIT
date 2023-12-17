if __name__ == '__main__':
    a = list(map(int, input().split()))
    while len(a) != 10:
        a += list(map(int, input().split()))
    ans = set([x % 42 for x in a])
    print(len(ans))