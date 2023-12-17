n, m = 3, 4

a = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        print(a[i][j], end=' ')
    print()

arr = [None] * n
for i in range(n):
    arr[i] = list(map(int, input().split()))

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()

# tìm min, max của arr 2 chiều
min_val, max_val = 10**18, -10**18
for row in arr:
    min_val = min(min_val, min(row))
    max_val = max(max_val, max(row))
print(min_val, max_val)

# Flatten mảng 2 chiều thành mảng 1 chiều
a = [[1, 2, 5], [3, 1, 0], [4, 1, 5]]
b = [x for small_list in a for x in small_list]
print(max(b))
print(max(b))
print(b)

# Tính tổng trên từng hàng của ma trận
a = [[1, 2, 5], [3, 1, 0], [4, 1, 5]]
sum_row = [sum(row) for row in a]
print(*sum_row)

# Ma trận chuyển vị
a_t = [[row[i] for row in a] for i in range(len(a[0]))]
b_t = [[a[i][j] for i in range(len(a))] for j in range(len(a[0]))]
print(a_t)
print(b_t)