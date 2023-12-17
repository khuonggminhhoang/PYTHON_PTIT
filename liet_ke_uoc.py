n = int(input())
s = ""
cnt = 0
for i in range(1, n + 1):
    if n % i == 0 :
        cnt+=1
        s += str(i) + " "
print(cnt)
print(s)