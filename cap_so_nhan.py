a, b, c, d = map(float, input().split())
cb = b/a
if b * cb == c and c * cb == d :
    print('YES')
else :
    print('NO')