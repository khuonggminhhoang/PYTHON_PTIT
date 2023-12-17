if __name__ == '__main__' : 
    m = int(input())
    ans = 0
    ans += m//100
    m%= 100
    ans += m//20
    m %= 20
    ans += m//10
    m %= 10
    ans += m//5
    m %= 5
    ans += m
    print(ans)
