if __name__ == '__main__':
    dct = {
        '5' : 10000,
        '7' : 15000,
        '2' : 20000,
        '29' : 50000,
        '45' : 70000
    }

    ans = dict()
    for _ in range(int(input())):
        s = input().split()
        if s[3] == 'IN':
            if s[4] in ans.keys():
                ans[s[4]] += dct[s[2]]
            else:
                ans[s[4]] = dct[s[2]]

    for key, val in ans.items():    
        print(key, val, sep=': ')