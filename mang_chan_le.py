from sys import stdin

if __name__ == '__main__':
    a = []
    for sys in stdin:
        # a += list(map(int, input().split()))
        a.extend(list(map(int, input().split())))

    cntEven = 0
    cntOdd = 0
    for x in a:
        if x % 2 == 0:
            cntEven +=1 
        else:
            cntOdd += 1
    if cntEven > cntOdd:
        print('CHAN')
    elif cntOdd > cntEven:
        print('LE')
    else:
        print('CHANLE')

