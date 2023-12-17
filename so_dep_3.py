def increase_number(n):
    for i in  range(1, len(n)):
        if n[i-1] > n[i]:
            return False
    return True

def decrease_number(n):
    for i in range(1, len(n)):
        if n[i - 1] < n[i]:
            return False
    return True

if __name__ == '__main__':
    s = input()
    if increase_number(s) or decrease_number(s):
        print('YES')
    else:
        print('NO')