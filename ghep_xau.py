from functools import cmp_to_key

def comp(a, b):
    ab = a + b
    ba = b + a
    if(ab > ba):
        return -1
    else:
        return 1

if __name__ == '__main__':
    n = int(input())
    arr = input().split()
    arr.sort(key= cmp_to_key(comp))
    print(''.join(arr))