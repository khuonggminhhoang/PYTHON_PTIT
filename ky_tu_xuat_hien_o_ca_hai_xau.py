if __name__ == '__main__':
    s1 = input()
    s2 = input()
    set1 = set(s1)
    set2 = set(s2)

    inter = set1.intersection(set2)
    for x in sorted(inter):
        print(x, end='')
    print()

    uni = set1.union(set2) 
    for x in sorted(uni):
        print(x, end='')

    