a, b, n = map(int, input().split())
flag = False
for x in range(n//a + 1):
    if (n-a*x) % b == 0:
        flag = True
        break
print('YES' if flag else 'NO')
