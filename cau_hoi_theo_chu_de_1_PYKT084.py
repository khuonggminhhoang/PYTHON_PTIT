if __name__ == '__main__':
    n = int(input())
    dct = dict()
    is_topic = True
    topic = ''
    for _ in range(n):
        s = input()
        if is_topic:
            topic = s
            dct[topic] = 0
            is_topic = False
            continue

        if len(s) == 0:
            is_topic = True
            continue
        dct[topic] += 1
      
    for x in dct:
        print(f'{x}: {dct[x]}')