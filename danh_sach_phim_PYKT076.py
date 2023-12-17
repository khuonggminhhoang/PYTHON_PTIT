class Film:
    cnt = 0

    def __init__(self, id_cat, date, name, episode):
        Film.cnt += 1
        self.__id = f'P{Film.cnt:03d}'
        self.__id_cat = id_cat
        self.__date = date
        self.__name = name
        self.__episode = episode

    def get_id(self):
        return self.__id

    def get_cat_id(self):
        return int(self.__id_cat[4])

    def set_cat(self, cat_name):
        self.__cat_name = cat_name

    def get_date(self):
        arr = self.__date.split('/')
        arr = arr[::-1]
        return int(''.join(arr))

    def get_name_film(self):
        return self.__name
    
    def get_episode(self):
        return self.__episode
    
    def __str__(self):
        return f'{self.__id} {self.__cat_name} {self.__date} {self.__name} {self.__episode}'

if __name__ == '__main__':
    n, m = map(int, input().split())
    lst = [0]
    for _ in range(n):
        lst.append(input())

    arr = []
    for _ in range(m):
        film = Film(input(), input(), input(), int(input()))
        for i in range(1, n + 1):
            if i == film.get_cat_id():
                film.set_cat(lst[i])
        arr.append(film)
    arr.sort(key= lambda x : (x.get_date(), x.get_id(), -x.get_episode()))
    print(*arr, sep='\n')