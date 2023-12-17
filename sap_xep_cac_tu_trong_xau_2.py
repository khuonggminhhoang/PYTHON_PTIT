if __name__ == '__main__':
    a = input().split()
    b = []
    se = set()
    for x in a:
        if x == x[::-1] and x not in se:
            b.append(x)
            se.add(x)
    b.sort(key= lambda x : len(x))
    print(' '.join(b))
            