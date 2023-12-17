if __name__ == '__main__':
    n = int(input())
    a = set(map(int, input().split()))
    q = int(input())
    while q:
        num = int(input())
        print('YES' if num in a else 'NO')
        q -= 1
