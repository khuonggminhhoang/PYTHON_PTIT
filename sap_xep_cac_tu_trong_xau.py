from functools import cmp_to_key 

def cmp1(s1, s2):
    return len(s1) - len(s2)

def cmp2(s1, s2):
    if len(s1) != len(s2):
        return len(s1) - len(s2)
    else:
        return (s1 > s2) - (s1 < s2)

def cmp(s1, s2):
    return (s1 > s2) - (s1 < s2)
    # return > 0 nếu s1 > s2

if __name__ == '__main__':
    arr = input().split()
    for x in sorted(arr, key= cmp_to_key(cmp)):
        print(x, end=' ')
    print()

    b = sorted(arr, key = cmp_to_key(cmp2))
    for x in b:
        print(x, end=' ')

