from functools import cmp_to_key

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
        self.__id = f'{Student.cnt:04d}'
        self.__classs = classs
        self.__gpa = gpa

    def get_name(self):
        return self._name

    def get_id(self):
        return self.__id

    def __str__(self):
        return self.__id + ' ' + super().__str__() + ' ' + self.__classs + ' ' + f'{self.__gpa:.2f}'

def cmp(o1, o2):
    arr1 = o1.get_name().split()
    arr2 = o2.get_name().split()
    s1 = arr1[-1] + ' ' + ' '.join(arr1[:-1])
    s2 = arr2[-1] + ' ' + ' '.join(arr2[:-1])
    if s1 != s2:
        return (s1 > s2) - (s1 < s2)
    else:
        return (o1.get_id() > o2.get_id()) - (o1.get_id() < o2.get_id())

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
        
    arr.sort(key = cmp_to_key(cmp))
    for x in arr:
        print(x)