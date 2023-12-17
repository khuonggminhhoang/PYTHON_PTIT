if __name__ == '__main__':
    a, b, c = map(int, input().split())
    if not( a + b > c and a + c > b and b + c > a) :
        print('INVALID')
    elif a == b ==c:
        print(1)
    elif a == b or b == c or a == c:
        print(2)
    elif (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
        print(3)
    else : print(4)