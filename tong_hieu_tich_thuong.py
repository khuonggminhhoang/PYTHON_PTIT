if __name__ == '__main__' :
    a, b = map(int, input().split())
    print(a + b)
    print(a-b)
    print(a*b)
    if b!=0 :
        print('%.4f' %(a/b))
    else:
        print('INVALID')