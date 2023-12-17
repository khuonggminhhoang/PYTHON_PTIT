if __name__ == '__main__':
    s = input()
    target = 'python'
    index = 0
    for x in s:
        if x == target[index]:
            index += 1
            if index == 6:
                break
    print('YES' if index == 6 else 'NO')