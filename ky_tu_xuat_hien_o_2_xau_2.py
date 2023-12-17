if __name__ == '__main__':
    s1 = input()
    s2 = input()
    set1 = set(s1)
    set2 = set(s2)
    arr = set1.difference(set2)
    print(''.join(sorted(arr)))

    arr = set2.difference(set1)
    print(''.join(sorted(arr)))