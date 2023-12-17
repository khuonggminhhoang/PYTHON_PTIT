a, b, k = map(int, input().split())
ans = k//2 * a - k//2 * b + k%2*a
print(ans)