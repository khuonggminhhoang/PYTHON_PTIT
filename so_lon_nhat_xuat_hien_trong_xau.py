if __name__ == '__main__':
    s = input()
    tmp = ''
    for x in s:
        if x.isalpha():
            tmp += ' '
        else:
            tmp += x
    arr = list(map(int, tmp.split()))
    print(max(arr))