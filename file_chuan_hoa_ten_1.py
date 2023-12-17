def nameStd(name) -> str:
    name = name.strip().split()
    return ' '.join(name).title()

if __name__ == '__main__':
    inp = open('input.txt', 'r')
    out = open('output.txt', 'w')

    line = inp.read()
    fullnames = line.split(',')
    for fullname in fullnames:
        out.write(nameStd(fullname))
        if fullname != fullnames[-1]:
            out.write(',')

    inp.close()
    out.close()