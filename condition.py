if __name__ == "__main__":
    n = int(input())
    #1
    if n % 2 == 0 :
        print('YES')
    else :
        print('NO')
    #2
    if n%3 == 0 and n%5 == 0:
        print('YES')
    else:
        print('NO')
    #3
    if n%3 == 0 and n%7 != 0 :
        print('YES')
    else:
        print('NO')

    #4
    if n%3 == 0 or n%7 == 0 :
        print('YES')
    else:
        print('NO')
    
    #5
    if 30 < n and n < 50 :
        print('YES')
    else:
        print('NO')
    
    #6
    if n >= 30 and (n%2 == 0 or n%3 == 0 or n%5 == 0) :
        print('YES')
    else:
        print('NO')
    
    #7
    tmp = n%10
    if 10 <= n and n <= 99 and (tmp == 2 or tmp == 3 or tmp == 5 or tmp ==7):
        print('YES')
    else:
        print('NO')
    
    #8
    if n <= 100 and n%23 == 0 :
        print('YES')
    else:
        print('NO')
    
    #9
    if n < 10 or n > 20:
        print('YES')
    else:
        print('NO')
    #10
    if tmp % 3 == 0:
        print('YES')
    else:
        print('NO')
    
    
