from sys import stdin

if __name__ == '__main__':
    n = int(input())
    dct = {}
    for i in range(1, n + 1):
        dct[i] = []
        
    for line in stdin:
        a, b = map(int, line.split())
        dct[a] += [b]
        dct[b] += [a]
        
    flag = False
    for x in dct:
        if len(dct[x]) == n - 1:
            flag = True
            
    print('Yes' if flag else 'No')