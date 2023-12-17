if __name__ == '__main__':
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    st1 = set(a)
    st2 = set(b)
    print(*sorted((st1.intersection(st2))))
    print(*sorted(st1.difference(st2)))
    print(*sorted(st2.difference(st1)))
