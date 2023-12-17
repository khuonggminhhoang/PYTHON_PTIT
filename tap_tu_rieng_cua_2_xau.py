if __name__ == '__main__':
    set1 = set(input().lower().split())
    set2 = set(input().lower().split())
    diff = set1.difference(set2)
    print(*sorted(diff))