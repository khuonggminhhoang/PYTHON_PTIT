import re

if __name__ == '__main__':
    ans = ''
    while True:
        try:
            ans += input()
        except :
            break

    arr = re.split('[.!?]', ans)
    arr.remove('')
    for line in arr:
        line = line.strip().capitalize()
        a = line.split()
        line = ' '.join(a)
        print(line)