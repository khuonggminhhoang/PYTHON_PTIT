#----Hoang Minh Khuong----#
from sys import stdin

const = 20000001

def seive():
    dct = {}
    for i in range(1, const):
        dct[i] = [1]
    
    for i in range(2, const):
        for j in range(i, const, i):
            dct[j].append(i)

    lst = []
    tmp = 0
    for x in dct:
        if len(dct[x]) > tmp:
            lst +=[x]
            tmp = len(dct[x])
    return lst
#--------- hàm này trả về list các số phản nguyên tố nhỏ nhất -------------#

if __name__ == '__main__':
    lst = [1, 2, 4, 6, 12, 24, 36, 48, 60, 120, 180, 240, 360, 720, 840, 1260, 1680, 2520, 5040, 7560, 
    10080, 15120, 20160, 25200, 27720, 45360, 50400, 55440, 83160, 110880, 166320, 221760, 277200, 
    332640, 498960, 554400, 665280, 720720, 1081080, 1441440, 2162160, 2882880, 3603600, 4324320, 6486480, 
    7207200, 8648640, 10810800, 14414400, 17297280]
    N = lst[43]
    ans = [0]*(N+1)
    ans[0]=ans[1]=1
    for i in range(1, 44):
        for j in range(lst[i-1]+1, lst[i]+1): ans[j] = lst[i]
    t = int(stdin.readline())
    while t:
        n = int(stdin.readline())
        if n<=N: print(ans[n])
        else:
            for i in range(44,len(lst)):
                if n<=lst[i]:
                    print(lst[i])
                    break
        t -= 1
    
#Note: dùng stdin đọc dữ liệu nhanh hơn