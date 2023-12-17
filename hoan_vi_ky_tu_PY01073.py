def Try(arr):
    global n
    if len(arr) == n:
        print(arr)
        return
    for j in range(0, n):
        if used[j] == False:
            used[j] = True
            Try(arr + s[j])
            used[j] = False

if __name__ == '__main__':
    s= input()
    n = len(s)
    used = [False] * len(s)
    Try('')
    print((2, 3))
