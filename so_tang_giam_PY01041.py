def solve(s):
    if len(s) < 3:
        return False
    id = 0
    while id < len(s) - 1 and s[id] < s[id + 1]:
        id += 1
    
    while id < len(s) - 1 and s[id] > s[id + 1]:
        id += 1
    
    return id == len(s) - 1
    

if __name__ == '__main__':
    t = int(input())
    while t :
        s = input()
        print('YES' if solve(s) else 'NO')
        t -= 1