def Try(s, cnt2, cnt3, cnt5, cnt7, n):
    if len(s) == n and s[len(s)-1] != '2' and cnt2 > 0 and cnt3 > 0 and cnt5 > 0 and cnt7 > 0:
        print(s)
    elif len(s) < n:
        Try(s + '2', cnt2 + 1, cnt3, cnt5, cnt7, n)
        Try(s + '3', cnt2 ,cnt3 + 1, cnt5, cnt7, n)
        Try(s + '5', cnt2, cnt3, cnt5 + 1, cnt7, n)
        Try(s + '7', cnt2, cnt3, cnt5, cnt7 + 1, n)

if __name__ == '__main__':
    n = int(input())
    for i in range(4, n + 1):
        Try('', 0, 0, 0, 0, i)
