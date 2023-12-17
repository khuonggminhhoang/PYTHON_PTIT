import queue

def check(n):
    cnt2 = n.count('2')
    return cnt2 > len(n)//2

if __name__ == '__main__':
    t = int(input())
    while t :
        n = int(input())
        i = 0
        que = queue.Queue()
        que.put('1')
        que.put('2')
        while not que.empty():
            x = que.get()
            if i >= n: break
            if check(x):
                print(x, end=' ')
                i += 1

            que.put(x + '0')
            que.put(x + '1')
            que.put(x + '2')
        print()
        t -= 1