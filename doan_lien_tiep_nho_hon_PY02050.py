if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        a = list(map(int, input().split()))
        stk = [-1]
        ans = []
        for i in range(n):
            while stk[-1] != -1 and a[stk[-1]] <= a[i]:
                stk.pop()
            ans.append(i - stk[-1])
            stk.append(i)
        t -= 1
        print(*ans)

'''
Cách 2: lâu hơn 

from queue import LifoQueue

if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        a = list(map(int, input().split()))
        stack = LifoQueue()
        stack.put(-1)

        ans = []
        for i in range(n):
            while stack.queue[-1] != -1 and a[stack.queue[-1]] <= a[i]:
                stack.get()
            ans.append(i - stack.queue[-1])
            stack.put(i)

        print(*ans)
        t -=1

'''