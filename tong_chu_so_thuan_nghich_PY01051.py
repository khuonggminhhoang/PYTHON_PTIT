def sum_digit(s):
    sum = 0
    for x in s:
        sum += int(x)
    return sum

if __name__ == '__main__':
    t = int(input())
    while t:
        s = input()
        tmp = sum_digit(s)
        print('YES' if tmp == int(str(tmp)[::-1]) and tmp > 9 else 'NO')
        t -= 1