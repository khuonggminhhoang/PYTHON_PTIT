if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    b = a[::-1] # lật ngược mảng
    print('YES' if a == b else 'NO')
