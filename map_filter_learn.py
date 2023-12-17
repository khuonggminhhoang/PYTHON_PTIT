from math import *

"""
    map() là một hàm trong python có chức năng apply một hàm có sẵn cho mọi
    phần tử trong một iterable (list, tuple, str...)

    form:
        map(function, iterable)

        
    filter() được sử dụng để trích xuất các phần tử trong một iterable khi
    apply một hàm nào đó với phần tử nào đó mà hàm trả về giá trị true

    form:
        filter(function, iterable)

"""
def even(n):
    return n%2 == 0

def isPrime(n):
    if n < 2: return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def add(a, b):
    return a + b

def square(a):
    return a ** 2

if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    b = list(map(square, a))
    print(b)

    # có thể sử dụng hàm lambda cho gọn
    c = list(map(lambda x : x**2, a))
    print(c)

    # có thể áp dụng map với nhiều iterable
    a = [0, 2, 4, 6, 8]
    b = [1, 3, 5, 7, 9]
    c = list(map(add, a, b))
    # dùng hàm lambda
    d = list(map(lambda x, y: x - y, a, b))

    print(c)
    print(d)

    # filter:

    a = [1, 2, 3, 5, 8, 7, 11, 17, 18, 19]
    b = [x for x in a if isPrime(x)]   #list comprehension
    print(b)

    c = list(filter(isPrime, a))    # filter
    print(c)

    odd = list(filter(lambda x : x % 2 == 1, a))    # dùng hàm lambda
    print(odd)