def sum_digit(n):
    num = 0
    while(n != 0):
        num += n%10
        n //= 10
    return num

def cmp(x):
    return x[1]

if __name__ == '__main__':
    # sort(key = ..., reverse =...true/false...)
    # false sx tăng dần
    # true sx giảm dần

    a = [2, -13, -35, 41, 9, -7, 44, 25]
    print(a)
    # a.sort()     #sx tăng dần
    # a.sort(reverse=True)    #sx giảm dần
    # a.sort(key= sum_digit, reverse = True)
    a.sort(key= lambda x : abs(x))
    print(sorted(a, key= lambda x: abs(x)))
    print(a)

    b = [[1,3], [2,-4], [5,7],[0,-3], [0, 10]]

    # b.sort(key= lambda x : x[0], reverse=True)
    b.sort(key= lambda x : (x[0], -x[1]))
    # b.sort(key = cmp, reverse=True)
    print(b)
    