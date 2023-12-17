class GiaoVien:
    def __init__(self, id, name, sal):
        self.__id = id
        self.__name = name
        self.__sal = sal

    def getAllowance(self):
        s = self.__id[0:2]
        if s == 'HT': return 2000000
        elif s == 'HP': return 900000
        elif s == 'GV': return 500000
        else: return 0

    def getLevel(self):
        return int(self.__id[2:])

    def total(self):
        return self.__sal * self.getLevel() + self.getAllowance()
    
    def __str__(self):
        return f'{self.__id} {self.__name} {self.getLevel()} {self.total()}'

if __name__ == '__main__':
    gv = GiaoVien(input(), input(), int(input()))
    print(gv)