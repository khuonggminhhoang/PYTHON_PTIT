def cnt_row(lst, n):
    ans = 0
    for sub in lst:
        cnt = 0
        for c in sub:
            if c == 'C':
                cnt += 1
        ans += cnt * (cnt - 1)//2
    return ans

def cnt_col(lst, n):
    ans = 0
    for j in range(n):
        cnt = 0
        for i in range(n):
            if lst[i][j] == 'C':
                cnt += 1
        ans += cnt * (cnt - 1)//2
    return ans

if __name__ == '__main__':
    n = int(input())
    a = [0] * n
    for i in range(n):
        a[i] = list(input())
    print(cnt_row(a, n) + cnt_col(a, n))