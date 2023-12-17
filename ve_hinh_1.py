n = int(input())

for i in range(n):
    for j in range(n):
        print('*', end= '')
    print()

print()

for i in range(n):
    for j in  range(n):
        if (i!=0 and i != n-1 and j != 0 and j!= n-1): print(' ',end='')
        else: print('*', end='')
    print()
print()

for i in range(n):
    for j in range(n):
        if i != 0 and i != n-1 and j != 0 and j != n-1 :
            print('#', end= '')
        else:
            print('*', end='')
    print()
print()

for i in range(1, n+1):
    for j in range(1, n+1):
        if i != 1 and i != n and j != 1 and j != n :
            print(' ', end= '')
        else : 
            print(i, end = '')
    print()