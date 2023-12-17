class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __str__(self):
        return f'{self.__name} {self.__age}'

class Student(Person):
    def __init__(self, id, name, age):
        # super().__init__( name, age)
        Person.__init__(self, name, age)
        self.__id = id

    # Overriding
    def __str__(self):
        # return f'{self.__id} {super().__str__()}'
        return f'{self.__id} {Person.__str__(self)}'

# Có thể dùng hàng super(...).method để dùng các phương thức của lớp cha
# hoặc dùng [tên Cha].method(self, ...)

if __name__ == '__main__':
    x = Student('B21DCCN461', 'Khuong', '20')
    print(x) 
