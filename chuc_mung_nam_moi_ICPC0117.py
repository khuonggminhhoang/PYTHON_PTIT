if __name__ == '__main__':
    t = int(input())
    s = set()
    while t:
        s.add(input())
        t -= 1
    print(len(s))
    
