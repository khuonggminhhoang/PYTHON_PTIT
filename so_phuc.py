class SoPhuc:
    def __init__(self, thuc, ao):
        self.__thuc = thuc
        self.__ao = ao

    #  nạp chồng toán tử + - * /
    
    def __add__(self, other):
        thuc = self.__thuc + other.__thuc
        ao = self.__ao + other.__ao
        return SoPhuc(thuc, ao)
    
    def __sub__(self, other):
        thuc = self.__thuc - other.__thuc
        ao = self.__ao - other.__ao
        return SoPhuc(thuc, ao)
    
    def __mul__(self, other):
        thuc = self.__thuc * other.__thuc - self.__ao * other.__ao
        ao = self.__thuc * other.__ao + self.__ao * other.__thuc
        return SoPhuc(thuc, ao)
    
    def __truediv__(self, other):
        mau = other.__thuc ** 2 + other.__ao ** 2
        thuc = (self.__thuc * other.__thuc + self.__ao * other.__ao) / mau
        ao = (self.__ao * other.__thuc - self.__thuc * other.__ao) / mau
        return SoPhuc(thuc, ao)

    #  nạp chồng toán tử 
    '''
        __lt__: < less than 
        __le__: <= less than or equal
        __gt__: > greater than
        __ge__: >= greater than or equal
        __eq__: == equal
        __ne__: != not equal
    
    '''
    def __eq__(self, other):
        return self.__thuc == other.__thuc and self.__ao == other.__ao

    def __ne__(self, other):
        return self.__thuc != other.__thuc or self.__ao != other.__ao

    def __str__(self):
        return f'{self.__thuc} + {self.__ao}j'

if __name__ == '__main__':
    s1 = SoPhuc(2, 3)
    s2 = SoPhuc(3, 1)
    s3 = s1 + s2
    s4 = s1 - s2
    s5 = s1 * s2
    s6 = s1 / s2
    print(s1)
    print(s2)
    print(s3)
    print(s4)
    print(s5)
    print(s6)
    print(s1 == s1)
    print(s1 != s1)