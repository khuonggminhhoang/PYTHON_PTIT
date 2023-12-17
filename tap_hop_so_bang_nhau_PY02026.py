if __name__ == '__main__':
    n, m = map(int, input().split())
    a = set(list(map(int, input().split())))
    b = set(list(map(int, input().split())))
    a = sorted(a)
    b = sorted(b)
    print('YES' if a == b else 'NO')