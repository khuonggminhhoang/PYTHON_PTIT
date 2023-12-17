if __name__ == '__main__':
    set1 = set(input().lower().split())
    set2 = set(input().lower().split())
    inter = set1.intersection(set2)
    print(*sorted(inter))