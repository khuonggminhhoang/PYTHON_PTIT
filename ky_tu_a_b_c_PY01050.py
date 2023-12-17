def Try_(s, n, a, b, c):
    if len(s) == n and 0 < a and a <= b and b <= c:
        print(s)
    if len(s) < n:
        Try_(s + 'A', n, a + 1, b, c)
        Try_(s + 'B', n, a, b  + 1, c)
        Try_(s + 'C', n, a, b, c + 1)

if __name__ == '__main__':
    n = int(input())
    for i in range(3, n + 1):
        Try_('', i, 0, 0, 0)