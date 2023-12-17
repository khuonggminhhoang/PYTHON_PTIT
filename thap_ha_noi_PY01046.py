def tower(n, a, b, c):
    if n  == 1:
        print(a, '->', c)
    else:
        tower(n-1, a, c, b)     # chuyển n - 1 đĩa từ cọc a sang cọc b
        print(a, '->', c)       # chuyển đĩa n sang cọc c
        tower(n-1, b, a, c)     # chuyển n-1 đĩa từ cọc b sang cọc c

if __name__ == '__main__':
    n = int(input())
    tower(n, 'A', 'B', 'C')