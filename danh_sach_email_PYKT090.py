if __name__ == '__main__':
    file = open('CONTACT.in', 'rt')
    s = file.read().splitlines()
    st = set()
    for line in s:
        st.add(line.lower())
    st = list(st)
    st.sort()
    for x in st:
        print(x)