if __name__ == '__main__':
    t = int(input())
    while t :   
        num = input() 
        sub_num = input()
        num.find(sub_num)
        num = num.replace(sub_num,'_')
        print(num.count('_'))
        t -= 1