def arr_equals(arr):
    for i in range(len(arr) - 1):
        if arr[i] != arr[i+1]:
            return False
    return True

if __name__ == '__main__':
    while True:
        a = list(map(int, input().split()))
        cnt = 0
        if a[0] == 0 and arr_equals(a):
            break
        while True:
            if arr_equals(a):
                print(cnt)
                break
            else:
                tmp = a[0]
                for i in range(3):
                    a[i] = abs(a[i] - a[i + 1])
                a[3] = abs(a[3] - tmp)
                cnt += 1
