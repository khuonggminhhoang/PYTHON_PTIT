def convertBin(n):
    if n == 0: return
    convertBin(n//2)
    print(n%2, end = '')

if __name__ == '__main__':
    n = int(input())
    if n == 0 :
        print(0)
        exit(0)
    convertBin(n)