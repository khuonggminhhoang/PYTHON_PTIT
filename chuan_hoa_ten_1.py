def nameStd(name):
    a = name.split()
    a = ' '.join(a).title()
    return a

def dayStd(day):
    if day[1] == '/':
        day = '0' + day
    if day[4] == '/':
        day = day[0:3] + '0' + day[3:]
    return day

if __name__ == '__main__':
    name = input()
    day = input()
    print(nameStd(name))
    print(dayStd(day))