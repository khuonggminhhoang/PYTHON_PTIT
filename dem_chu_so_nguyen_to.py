n = int(input())
cnt = 0
while n!= 0:
    tmp = n%10
    if( tmp == 2 or tmp == 3 or tmp == 5 or tmp == 7):
        cnt += 1
    n//=10
print(cnt)