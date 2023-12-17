def rotate_string(s, step):
    return s[step:] + s[:step]

def min_rotation(arr):
    ans = 10**18
    for target in arr:
        total_step = 0
        for x in arr:
            flag = False
            for i in range(len(target)):
                if rotate_string(x, i) == target:
                    total_step += i
                    flag = True
                    break
            if not flag:
                return -1
        ans = min(ans, total_step)
    return ans

if __name__ == '__main__':
    n = int(input())
    a = []
    for _ in range(n):
        a.append(input())
    print(min_rotation(a))
