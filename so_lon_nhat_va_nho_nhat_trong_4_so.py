a, b , c , d = map(int, input().split())
minVal = 1e18 + 1
maxVal = -1e18 - 1

minVal = min(minVal, a)
minVal = min(minVal, b)
minVal = min(minVal, c)
minVal = min(minVal, d)

maxVal = max(maxVal, a)
maxVal = max(maxVal, b)
maxVal = max(maxVal, c)
maxVal = max(maxVal, d)
print(maxVal, minVal)