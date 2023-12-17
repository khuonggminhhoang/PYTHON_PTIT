# if __name__ == '__main__':
#     t = int(input())
#     while t:
#         s1 = input()
#         s2 = input()
#         while s2 in s1:
#             tmp = s1.index(s2)
#             print(tmp + 1, end=' ')
#             s1 = s1[:tmp] + '_' + s1[tmp + 1:]
#         print()
#         t -= 1

'''
    aaaaa
    aa
    _aaaa
    
    

'''

# from  datetime import  datetime
#
# class SinhVien:
#     def __init__(self, name, timeIn, timeOut):
#         self.__name = name
#         self.__timeIn = timeIn
#         self.__timeOut = timeOut
#
#     def get_time(self):
#         formm = '%d/%m/%Y %H:%M:%S'
#         timeIn = datetime.strptime(self.__timeIn, formm)
#         timeOut = datetime.strptime(self.__timeOut, formm)
#         return (timeOut - timeIn).seconds//60
#
#     def __str__(self):
#         return f'{self.__name} {self.get_time()}'
#
# if __name__ == '__main__':
#     file = open('ONLINE.in', 'rt')
#     t = int(file.readline().strip())
#     lst = []
#     for _ in range(t):
#         lst.append(SinhVien(file.readline().strip(), file.readline().strip(), file.readline().strip()))
#
#     lst.sort(key=lambda x: -x.get_time())
#     print(*lst, sep='\n')

# def read_binary_file(filename):
#     data = []
#     with open(filename, 'rb') as file:
#         while True:
#             try:
#                 number = int.from_bytes(file.read(4), byteorder='big')
#                 data.append(number)
#             except ValueError:
#                 break
#     return data

# def read_binary_file(filename):
#     data = []
#     file = open(filename, 'rb')
#     while True:
#         try:
#             number = int.from_bytes(file.read(4), byteorder='big')
#             data.append(number)
#         except ValueError:
#             break
#     return data

def read_binary_file(filename):

    data = []
    file = open(filename, 'rb')
    while True:
        try:
            num = int.from_bytes(file.read(4), byteorder='big')
            data.append(num)
        except ValueError:
            break
    return data

def check(n):
    s = str(n)
    for i in range(1, len(s)):
        if int(s[i]) < int(s[i - 1]):
            return False
    return True

if __name__ == '__main__':
    lst1 = read_binary_file('DATA1.in')
    lst2 = read_binary_file('DATA2.in')
    dct1 = {}
    dct2 = {}
    for x in lst1:
        if check(x):
            if dct1.get(x):
                dct1[x] += 1
            else:
                dct1[x] = 1

    for x in lst2:
        if check(x):
            if dct2.get(x):
                dct2[x] += 1
            else:
                dct2[x] = 1
    lst = list(set(dct1.keys()))
    for x in lst:
        if x in dct2:
            print(x, dct1[x], dct2[x])
