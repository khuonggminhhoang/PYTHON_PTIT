if __name__ == '__main__':
    file1 = open('DATA1.in', 'rt')
    file2 = open('DATA2.in', 'rt')
    data1 = file1.read().lower().split()
    data2 = file2.read().lower().split()
    st1 = set(data1)
    st2 = set(data2)
    lst1 = list(st1.difference(st2))
    lst2 = list(st2.difference(st1))
    lst1.sort()
    lst2.sort()
    print(*lst1)
    print(*lst2)

