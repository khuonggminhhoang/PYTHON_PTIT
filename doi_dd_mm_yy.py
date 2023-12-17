if __name__ == '__main__':
    n = int(input())
    year = n//365
    n%=365
    week = n//7
    n%=7
    day = n
    print(year, week, day)
    