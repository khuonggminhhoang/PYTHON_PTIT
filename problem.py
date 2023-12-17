import math

if __name__ == '__main__':
    a, b, c = map(float, input().split())
    if a == 0:
        if b!=0 :
            ans = -1 *c/b
            print('%.2f' %(ans))
        elif c != 0 : print("VO NGHIEM")
        else : print("VO SO NGHIEM")
    else :
        delta = b*b - 4 *a*c
        if delta < 0 :
            print("VO NGHIEM")
        elif delta == 0:
            print('%.2f' % (-b/(2*a)))
        else :
            x1 = (-b + math.sqrt(delta))/(2*a)
            x2 = (-b - math.sqrt(delta))/(2*a)
            print('%.2f' %x2,'%.2f' %x1)

