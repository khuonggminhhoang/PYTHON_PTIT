if __name__ == '__main__':
    s = input()
    ans = 0
    tmp = ''
    for x in s:
        if x.isalpha():
            tmp += ' '
        else:
            tmp += x
    
    a = list(map(int, tmp.split()))
    print(sum(a))