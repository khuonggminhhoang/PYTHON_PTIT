from functools import cmp_to_key

def sum_digit(n):
    sum = 0
    while n != 0:
        sum += n%10
        n //= 10
    return sum

def cmp(a,b):
    o1 = sum_digit(a)
    o2 = sum_digit(b)
    if o1 != o2:
        return o1 - o2
    else:
        return a - b

if __name__ == '__main__':
    a = [10, 2, 4, 3, 5, 6, 0, 11, 56]
    a.sort(key = cmp_to_key(cmp))
    print(a)