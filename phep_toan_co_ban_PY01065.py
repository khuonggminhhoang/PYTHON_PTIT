def Try(i, s, tmp, lst_num):
    if i == len(s):
        lst_num += [tmp]
        return
    
    if s[i] == '?':
        if i == 0: 
            for j in range(1,10):
                Try(i + 1, s, tmp + str(j), lst_num)
        else:
            for j in range(10):
                Try(i + 1, s, tmp + str(j), lst_num)
    else:
        Try(i + 1, s, tmp + s[i], lst_num)

        
def isTrue(n1, n2, n3, operator):
    n1 = int(n1)
    n2 = int(n2)
    n3 = int(n3)
    if operator == '+': return n1 + n2 == n3
    if operator == '-': return n1 - n2 == n3
    if operator == '*': return n1 * n2 == n3
    if operator == '/': return n1 // n2 == n3
    return False
    
def solve(lst_num1, lst_num2, lst_num3, lst_operator):
    for n1 in lst_num1:
        for n2 in lst_num2:
            for n3 in lst_num3:
                for operator in lst_operator:
                    if isTrue(n1, n2, n3, operator):
                        return (n1 + ' ' + operator + ' ' + n2 + ' = ' + n3)
    return 'WRONG PROBLEM!'

if __name__ == '__main__':
    t = int(input())
    while t:
        s = input().split()
        n1 = s[0]
        operator = s[1]
        n2 = s[2]
        n3 = s[4]
        lst_num1 = []
        lst_num2 = []
        lst_num3 = []
        Try(0, n1, '', lst_num1)
        Try(0, n2, '', lst_num2)
        Try(0, n3, '', lst_num3)
        
        lst_operator = []
        if operator == '?':
            lst_operator += ['+', '-', '*', '/']
        else:
            lst_operator += operator
        
        print(solve(lst_num1, lst_num2, lst_num3, lst_operator))

        t -= 1