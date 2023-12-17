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
    t = int(input())
    a = []
    for _ in range(t):
        a.append( SinhVien(input(), input(), input(), input())) 
    a.sort(key = lambda x : (x.get_class(), x.get_id()))
    for x in a:
        print(x)