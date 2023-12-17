if __name__ == '__main__':
    s = input()
    ans1, ans2, ans3 = 0, 0, 0
    for x in s:
        if x.isalpha():
            ans1 += 1
        elif x.isdigit():
            ans2 += 1
        else:
            ans3 += 1
    print(ans1, ans2, ans3)