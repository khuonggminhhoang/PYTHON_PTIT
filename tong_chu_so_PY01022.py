n = input()
res = 0
while len(n) > 1:
    a = [(ord(i) - ord('0')) for i in n]
    n = str(sum(a))
    res += 1
print(res)