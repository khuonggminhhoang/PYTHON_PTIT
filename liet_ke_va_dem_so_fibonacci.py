fibo = [0] * 93

def fibonacci():
    global fibo
    fibo[0] = 0
    fibo[1] = 1
    for i in range(2, 93):
        fibo[i] = fibo[i-1]+ fibo[i-2]


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    fibonacci()
    for x in a:
        if x in fibo:
            flag = True
            print(x, end=' ')
    if not flag: print('NONE')
