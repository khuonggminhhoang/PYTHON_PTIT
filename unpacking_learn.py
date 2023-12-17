if __name__ == '__main__':
    s = "CR73"
    x, y, _, z= s
    print(x)
    print(y)
    print(z)
    a, b, c = range(0, 3, 1)
    print(a)
    print(b)
    print(c)

    a = [['A', 65], ['B', 66],['C', 67]]
    for ma, kitu in a:
        print(ma, '->', kitu)
    
    # unpacking với toán tử *
    a = [1, 2, 3, 4, 5, 6, 7, 8 ,9, 10]
    x, y, *_ = a
    print(x, y)
    x, *_, z, t = a
    print(x, z, t)

