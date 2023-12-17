def conv(n, base):
    ans = ''
    while n :
        ans += str(n%base)
        n //= base
    return ans == ans[::-1]

def palin_bin(n):
    tmp = bin(n)[2:]
    return tmp == tmp[::-1]

if __name__ == '__main__':
    a, b, m = map(int, input().split())

    pln_arr = [i for i in range(a, b + 1) if palin_bin(i)]
    for base in range(2, m + 1):
        pln_arr = [x for x in pln_arr if conv(x, base)]
        if len(pln_arr) == 0:
            break
    print(len(pln_arr))
    