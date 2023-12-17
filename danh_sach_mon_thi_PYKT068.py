class MonThi:
    def __init__(self, id, name, type) -> None:
        self.__id = id
        self.__name = name
        self.__type = type

    def get_id(self):
        return self.__id

    def __str__(self):
        return f'{self.__id} {self.__name} {self.__type}'

if __name__ == '__main__':
    n = int(input())
    lst = []
    for _ in range(n):
        lst.append(MonThi(input(), input(), input()))
    lst.sort(key= lambda x : x.get_id())
    print(*lst, sep='\n')
