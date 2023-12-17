import math

if __name__ == '__main__':
    n, m, a = map(int , input().split())
    print( math.ceil(n/a) * math.ceil(m/a))