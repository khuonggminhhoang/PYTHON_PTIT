def solve(a):
    dct = {}
    for x in a:
        if dct.get(x):
            dct[x] += 1
        else:
            dct[x] = 1
        
    st = list(set(dct.values()))
    st.sort()
    if len(st) < 2: return 'NONE'
    
    for x in dct:
        if dct[x] == st[-2]:
            return x
    return 'NONE'
    
if __name__ == '__main__':
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(a))