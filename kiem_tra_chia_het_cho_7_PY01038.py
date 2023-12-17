if __name__ == '__main__':
    t= int(input())
    while t:
        n = int(input())
        cnt = 0
        while cnt <= 1000:
            if n % 7 == 0:
                print(n)
                break
            n += int(str(n)[::-1])
            cnt += 1 
        t -= 1