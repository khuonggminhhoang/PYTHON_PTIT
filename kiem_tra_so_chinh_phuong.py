import math

def checkSquareNum(n):
    if math.sqrt(n) == math.isqrt(n):
        return True
    return False

if __name__ == '__main__':
    n = int(input())
    print('YES' if checkSquareNum(n) else 'NO')
