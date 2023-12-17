from queue import LifoQueue

if __name__ == '__main__':
    t = int(input())
    while t:
        s = input()
        ind = 1
        stack = LifoQueue()
        ans = ''
        for i in range(len(s)):
            if(s[i] == '('):
                stack.put(ind)
                ans += str(ind) + ' '
                ind += 1
            elif s[i] == ')':
                ans += str(stack.get()) + ' '
        print(ans)
        t -= 1