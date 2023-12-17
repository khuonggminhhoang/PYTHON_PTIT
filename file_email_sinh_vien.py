def email(s):
    arr = s.split()
    ans = ''
    ans += arr[-1].lower()
    arr = arr[0:-1]
    for x in arr:
        ans += x[0].lower()
    return ans + '@28land.edu.vn'

def password(s):
    arr = s.split('/')
    ans = ''
    for x in arr:
        ans += str(int(x))
    return ans

if __name__ == '__main__':
    inp = open('input.txt', 'rt')
    out = open('output.txt', 'wt')
    lst = inp.read().split('\n')
    for i in range(0, len(lst), 2):
        out.write(email(lst[i]) + '\n')
        out.write(password(lst[i + 1]) + '\n')

    inp.close()
    out.close()