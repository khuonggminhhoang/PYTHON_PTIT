def maxNum(s):
    a = []
    num  = ''
    for i in s:
        if i.isdigit() :
            num += i
        else:
            if len(num) != 0:
                a.append(int(num))
            num = ''
    if len(num) != 0:
        a.append(int(num))
    return max(a)

if __name__ == '__main__':
    t = int(input())
    while t:
        s = input()
        print(maxNum(s))
        t-=1


