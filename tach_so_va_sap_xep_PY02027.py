if __name__ == '__main__':
    t = int(input())
    lst = []
    for _ in range(t):
        s = input() + '_'
        num = ''
        for c in s:
            if c.isdigit():
                num += c
            else:
                if len(num) != 0:
                    lst.append(int(num))     
                num = ''
    lst.sort()
    print(*lst, sep='\n')
