a, b, c = map(int, input().split())
if a + b > c and b + c > a and a + c > b and a > 0 and b > 0 and c > 0:
    print('YES')
else:
    print('NO')