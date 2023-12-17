if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    for x in a:
        if len(b) == 0:
            b.append(x)
        else:
            tmp = b.pop()
            if (x + tmp) % 2 ==1:
                b.append(tmp)
                b.append(x)
    print(len(b))

