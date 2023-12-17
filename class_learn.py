class Person:
    # class attribute
    national = 'VIET NAM'
    
    def __init__(self, name, job, age):
        # name, job are instance attribute
        self.name = name    # public
        self.__job = job     # protected
        self.__age = age    # private
        
    def __greet(self):
        print('HELOOOO :3')
    
    def infor(self):
        self.__greet()
        print(self.name + ' ' + self.__job)

    def get_job(self):
        return self.__job
    
    def set_job(self, job):
        self.__job = job

    def __str__(self):
        # return '{} {} tuoi'.format(self.name, self.__age)
        return f'{self.name} {self.__job} {self.__age}'

if __name__ == '__main__':
    p1 = Person('Khuong', 'Dev', 20)
    p2 = Person('Dang', 'Tester', 20)
    
    # print(p1.__age) # lỗi vì __age là private attribute
    p1.infor()
    p2.infor()
    print(p1.get_job())
    p1.set_job('engineer')
    print(p1.get_job())
    # p1.__greet()

    print(p1.__repr__()) 
    print(p1.__str__())