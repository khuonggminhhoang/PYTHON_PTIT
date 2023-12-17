n = int(input())

for i in range(n):
    for j in range(i+1):
        print('*', end='')
    print()
print()

for i in range(n):
    for j in range(n-i):
        print('*', end='')
    print()
print()

for i in range(n):
    for j in range(n):
        if j < n-i-1 :
            print(' ', end='')
        else :
            print('*', end='')
    print()
print()
        
for i in range(n):
    for j in range(n):
        if j < i :
            print(' ', end= '')
        else :
            print('*', end='')
    print()
print()

for i in range(n):
    for j in range(i+1):
        if 0 < j < i and i != n-1:
            print(' ', end='')
        else :
            print('*', end='')
    print()
print()