def Try(i):
    global used, sub, lst, n
    for j in range(1, n + 1):
        if not used[j]:
            sub[i] = j
            used[j] = True
            if i == n: lst.append(''.join(map(str, sub[1:])))
            else: Try(i + 1)
            used[j] = False

if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        used = [False] * (n + 1)
        lst = []
        sub = [0] * (n + 1)

        Try(1)
        lst = lst[::-1]
        print(len(lst))
        print(*lst)

        t -= 1

    
    