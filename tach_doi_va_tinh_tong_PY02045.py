if __name__ == '__main__':
    s = input()
    while len(s) > 1:
        mid = len(s)//2
        s = int(s[:mid]) + int(s[mid:])
        s = str(s)
        print(s)