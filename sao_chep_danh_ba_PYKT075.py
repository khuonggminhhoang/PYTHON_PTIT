class DienThoai:
    def __init__(self, name, phone, day):
        self.__name = name
        self.__phone = phone
        self.__day = day

    def get_last_name(self):
        a = self.__name.split()
        return ' '.join(a[:-1])
    
    def get_first_name(self):
        a = self.__name.split()
        return a[-1]

    def __str__(self):
        return f'{self.__name}: {self.__phone} {self.__day}'

if __name__ == '__main__':
    f = open('SOTAY.txt', 'rt')
    lst = f.read().splitlines()
    f.close()
    a = []
    i = 0
    day = lst[1][5:]
    while i < len(lst):
        if lst[i][:4] == 'Ngay':
            day = lst[i][5:]
            i += 1
        else:
            name = lst[i]
            phone = lst[i + 1]
            a.append(DienThoai(name, phone, day))
            i += 2

    a.sort(key= lambda x : (x.get_first_name(), x.get_last_name()))
    f = open('DIENTHOAI.txt', 'wt')
    for x in a:
        f.writelines(x.__str__() + "\n")
    f.close()
    