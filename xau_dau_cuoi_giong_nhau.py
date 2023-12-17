if __name__ == '__main__':
    s = input()
    cnt = [0] * 256
    for x in s:
        cnt[ord(x)] += 1

    ans = len(s)
    for i in range(256):
        if cnt[i] != 0:
            ans += cnt[i] * (cnt[i] - 1)//2
    print(ans)