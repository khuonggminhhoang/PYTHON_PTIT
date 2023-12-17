if __name__ == '__main__':
    a, b, c, d = map(float, input().split())
    tb = (a + b + c*2 + d * 3)/ 7
    if tb >= 8:
        print('GIOI')
    elif 6.5 <= tb < 8:
        print('KHA') 
    elif 5 <= tb < 6.5:
        print('TRUNG BINH')
    else: print('YEU')