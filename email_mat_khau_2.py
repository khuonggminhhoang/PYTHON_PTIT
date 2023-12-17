def password(s):
    arr = s.split('/')
    ans = ''
    for x in arr:
        ans += str(int(x))
    return ans

def mail(s):
    arr = s.lower().split() 
    ans = arr[-1]
    for i in range(len(arr) - 1):
        ans += arr[i][0]
    return ans

if __name__ == '__main__':
    t = int(input())
    dct = dict()
    while t :
        s = input()
        arr = s.split()
        name = ''
        for i in range(len(arr) - 1):
            name += arr[i] + ' '

        shortedName = mail(name)
        if shortedName in dct:
            dct[shortedName] += 1
        else:
            dct[shortedName] = 1
        
        if dct[shortedName] == 1:
            print(shortedName + '@xyz.edu.vn')
        else:
            print(shortedName + str(dct[shortedName]) + '@xyz.edu.vn')
        print(password(arr[-1]))

        t -= 1