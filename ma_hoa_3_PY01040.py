def device(s):
    l = len(s)
    return s[:l//2], s[l//2:]

def total(s):
    tmp = 0
    for c in s:
        tmp += ord(c) - ord('A')
    return tmp

def rotate(s, tmp):
    ans = ''
    tmp %= 26
    for c in s:
        x = ord(c) - ord('A')
        if (x + tmp) > 25 :
            ans += chr(ord('A') + x + tmp - 26)
        else:
            ans += chr(ord('A') + x + tmp)
    return ans

def merge(s1, s2):
    ans = ''
    for i in range(len(s2)):
        ans += rotate(s1[i], ord(s2[i]) - ord('A'))
    return ans

if __name__ == '__main__':
    t = int(input())
    while t:
        s = input()
        s1, s2 = device(s)
        print(merge(rotate(s1, total(s1)), rotate(s2, total(s2))))
        t -= 1