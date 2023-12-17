if __name__ == '__main__':
    a, b = map(int, input().split())
    print(a//b * b)
    print((a+b-1)//b * b)