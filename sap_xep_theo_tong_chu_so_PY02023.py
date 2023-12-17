def sum_digit(s):
    sum = 0
    for x in s:
        sum += int(x)
    return sum

if __name__== '__main__':
    t = int(input())
    while t:
        n = int(input())
        a = input().split()
        a.sort(key = lambda x : (sum_digit(x), int(x)))
        for x in a:
            print(x, end=' ')
        print()
        t -= 1