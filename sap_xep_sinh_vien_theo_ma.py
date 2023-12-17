from sys import stdin

class SinhVien:
    def __init__(self, id, name, classs, email):
        self.__id = id
        self.__name = name
        self.__classs = classs
        self.__email = email
    
    def get_id(self):
        return self.__id

    def get_class(self):
        return self.__classs
    
    def __str__(self):
        return f'{self.__id} {self.__name} {self.__classs} {self.__email}'

if __name__ == '__main__':
    #  Cách 1
    # a = []
    # while True:
    #     try :
    #         a.append( SinhVien(input(), input(), input(), input())) 
    #     except :
    #         break
    # a.sort(key = lambda x : (x.get_id()))
    # for x in a:
    #     print(x)
    #  Cách 2:
    a = []
    line = []
    for x in stdin:
        line.append(x[:-1])
    for i in range(0, len(line), 4):
        a.append(SinhVien(line[i], line[i + 1], line[i + 2], line[i + 3]))
    a.sort(key = lambda x : x.get_id())
    for x in a:
        print(x)