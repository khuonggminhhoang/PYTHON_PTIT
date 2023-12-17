# a = [1, 2, 4, 3, 'Python', 'C++']
# for i in range(len(a)):
#     print(a[i] , end=' ')
# print()

# for i in range(-1, len(a)*-1 - 1, -1):
#     print(a[i], end=' ')
# print()

# a[0] = 'C#'

# for x in a :
#     print(x, end=' ')
# print()

# a.append(5000)
# a.append(1.4)

# a.insert(2, 'khuongminhhoang')
# a.insert(15, 90)

# print(a)
# a.pop(2) # xoa phan tu co index = 2
# a.pop() #xoa phan tu cuoi cung cua list
# del a[1] # xoa a[i] tring list a
# a.remove(5000) # xoa gia tri 5000 trong list
# print(a)
# # a.clear() : xoa list

# b = a * 3  # sao chep list a 3 lan gan vao list b
# print(b)

# tmp = [0] * 100
# print(tmp)

# a = [1,2,4,3,5]
# print(a)
# b = a       # ko gan 2 list,vi no cung tro den cung 1 id
# print(id(a))
# a.append(7)
# print(id(b))
# print(b)
# print(a is b)

# b = a.copy() 
# a.sort()
# print(a)
# print(b)
# print(a is b) # check xem a, b co cung dia chi o nho hay khong


# if 3 in a:
#     print('YES')
# else:
#     print('NO')

# print('YES' if 3 in a else 'NO')

# a = [1,2,3]
# b = [4,5,6]
# c = a.copy()
# a.extend(b) # nối list b vào list a
# print(b)
# print(a)

# c += 2*b
# print(c)

# # count(obj) : tra ve so luong phan tu obj trong list
# print(c.count(6))
# # index(obj): return the fisrt index of obj
# print(c.index(6))

# # reverse() : lat nguoc list
# c.reverse()
# print(c)

# # sort(): sap xep tang dan
# c.sort()
# print(c)

# # built-in function
# # sorted(list) : tra ve list da duoc sap xep tang dan
# d = sorted(c)
# print(d)
# print(c)

# # min(), max(), sum() 
# print(min(c), max(c), sum(c), sep='\n')
# # all(list): return True nếu mọi phần tử của list là True
# # any(list): return True nếu có ít nhất môt phần tử trong list là True
# c.append(0)
# print(all(c))
# print(any(c))

a = [1, 2, 3 , 4, 5 , 6 , 7 , 8 , 9 , 10]
for i in range(9, 2, -2):
    print(a[i])
print('-------------------')
for i in range(-1, -(len(a) + 1), -1):
    print(a[i])