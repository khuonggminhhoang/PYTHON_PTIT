class Team:
    cnt = 0

    def __init__(self, name, school):
        Team.cnt += 1
        self.__id = Team.cnt 
        self.__name = name
        self.__school = school

    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_school(self):
        return self.__school
    
class Student:
    cnt = 0

    def __init__(self, name, teamid):
        Student.cnt += 1
        self.__id = f'C{Student.cnt:03d}'
        self.__name = name
        self.__teamid = teamid

    def get_id_team(self):
        return int(self.__teamid[4:])

    def set_team(self, team):
        self.__team = team

    def get_name(self):
        return self.__name
    
    def __str__(self):
        return f'{self.__id} {self.__name} {self.__team.get_name()} {self.__team.get_school()}'

if __name__ == '__main__':
    t = int(input())
    lst = []
    for _ in range(t):
        lst.append(Team(input(), input()))

    t = int(input())
    arr = []
    for _ in range(t):
        std = Student(input(), input()) 
        for x in lst:
            if x.get_id() == std.get_id_team():
                std.set_team(x)
        arr.append(std)

    arr.sort(key= lambda x : x.get_name())
    print(*arr, sep='\n')