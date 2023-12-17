import re

def check(s):
    for c in s:
        if not c.isdigit(): return False
    return True

if __name__ == '__main__':
    file = open('DATA.in', 'rt')
    data = file.read()
    data = re.split('\\s+', data)
    ans = []
    for x in data:
        if check(x) == False:
            ans.append(x)
        elif len(x) > 9:
            ans.append(x)
    ans.sort()
    print(*ans)
