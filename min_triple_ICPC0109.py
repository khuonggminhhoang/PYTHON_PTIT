from sys import *

def find_min(arr, ans):
    for i in range(len(arr)):
        if ans > arr[i]:
            ans = arr[i]
            tmp = i
    arr[tmp] = maxsize
    return ans

if __name__ == '__main__':
    t = int(input())
    while t :
        n = int(input())
        a = list(map(int, input().split()))
        min1 = find_min(a, maxsize)
        min2 = find_min(a, maxsize)
        min3 = find_min(a, maxsize)
        print(min1 + min2 + min3)
        t -= 1