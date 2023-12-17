class Person:
    def __init__(self):
        pass

    def __init__(self, name, dob, addr):
        self._name = self.name_std(name)
        self._dob = self.day_std(dob)
        self._addr = addr

    def name_std(self, s):
        arr = s.strip().title().split()
        return ' '.join(arr)

    def day_std(self, s):
        if s[1] == '/':
            s = '0' + s
        if s[4] == '/':
            s = s[0:3] + '0' + s[3:]
        return s
    
    def __str__(self):
        return f'{self._name} {self._dob} {self._addr}'

class Student(Person):
    cnt = 0
    
    def __init__(self, name, dob, addr, classs, gpa):
        Student.cnt += 1
        Person.__init__(self, name, dob, addr)
        self.__id = f'{self.cnt:04d}'
        self.__classs = classs
        self.__gpa = gpa

    def __str__(self):
        return f'{self.__id} ' + super().__str__() + f' {self.__classs} {self.__gpa:.2f}'

if __name__ == '__main__':
    t = int(input())
    arr = []
    for _ in range(t):
        name = input()
        s = input()

        for i in range(len(s)):
            if s[i].isalpha():
                pos = i
                break
        
        dob = s[:pos]
        addr = s[pos:]
        classs = input()
        gpa = float(input())
        arr.append(Student(name, dob, addr, classs, gpa))
    
    for x in arr:
        print(x)

