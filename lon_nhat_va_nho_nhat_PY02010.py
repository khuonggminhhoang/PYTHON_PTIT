if __name__ == '__main__':
    while True:
        n = int(input())
        if n == 0: break
        lst = []
        for _ in range(n):
            lst += [int(input())]
        min_ = min(lst)
        max_ = max(lst)
        print('BANG NHAU' if min_ == max_ else f'{min_} {max_}')
