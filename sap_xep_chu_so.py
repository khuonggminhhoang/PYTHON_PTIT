if __name__ == '__main__':
    n = int(input())
    a = input().split()
    st = set()
    for x in a:
        for ele in x:
            st.add(ele)
    st = list(st)
    st.sort()
    for x in st:
        print(x, end=' ')