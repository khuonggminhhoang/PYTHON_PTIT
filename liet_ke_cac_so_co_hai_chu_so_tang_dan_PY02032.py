if __name__ == '__main__':
    s = input()
    if len(s) % 2 == 1:
        s = s[:-1]
    i = 0
    lst = []
    while i < len(s):
        lst += [int(s[i:i+2])]
        i += 2
    st = list(set(lst))
    st.sort()
    print(*st)