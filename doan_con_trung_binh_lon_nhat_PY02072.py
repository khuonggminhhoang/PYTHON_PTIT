def max_avg_len(a):
    cnt = 0
    m = max(a)
    ans = 0
    for x in a:
        if x == m:
            cnt +=1 
        else:
            ans = max(ans, cnt)
            cnt = 0
    ans = max(ans, cnt)
    return ans

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(max_avg_len(a))

# Note: đô dài dãy con tb lớn nhất chỉ cần xét các phần tử lớn nhất của dãy 