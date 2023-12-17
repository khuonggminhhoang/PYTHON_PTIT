class Student:
    cnt = 0

    def __init__(self, name, grade, ethnic, area):
        Student.cnt += 1
        self.__id = f'TS{Student.cnt:02d}'
        self.__name = self.name_std(name)
        self.__grade = grade
        self.__ethnic = ethnic
        self.__area = area

    def name_std(self, name):
        arr = name.strip().title().split()
        return ' '.join(arr)

    def get_priority(self):
        ans = 0
        if self.__area == 1: ans += 1.5
        elif self.__area == 2: ans += 1
        else: ans += 0
        
        if self.__ethnic.lower() != 'kinh':
            ans += 1.5
        return ans

    def get_total(self):
        return self.__grade + self.get_priority()

    def __str__(self):
        tmp = 'Do' if self.get_total() >= 20.5 else 'Truot'
        return f'{self.__id} {self.__name} {self.get_total()} {tmp}'

if __name__ == '__main__':
    t = int(input())
    lst = []
    for _ in range(t):
        lst.append(Student(input(), float(input()), input(), int(input())))
    lst.sort(key= lambda x : -x.get_total())
    print(*lst, sep='\n')
