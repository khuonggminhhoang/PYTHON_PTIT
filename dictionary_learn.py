'''
    + Dictionary là một cấu trúc dữ liệu thuộc dạng associative array hay hashmap
    + Nó bao gồm nhiều cặp key - value (key là duy nhất)


'''

infor = {
    'name' : 'Khương',
    'job' : 'student',
    'city' : 'Ha noi',
    'age' : 20.5
}
print(infor)
###################- - Khai Bao - -####################
# dùng constructor dict() để tạo 1 dictionary 
a = [['name', '28tech'], ['job', 'dev'], ['web', '28tech.com.vn']]
b = dict(a)
print(b)

# tạo dictionary bằng hàm zip()
a = ['name', 'job', 'web']
b = ['28tech', 'dev', '28tech.com.vn']
c = dict(zip(a, b))
print(c)
print(c)

# tạo dict bằng hàm fromkey
a = ['a', 'b', 'c']
value = 0
b = dict.fromkeys(a, value)
print(b)

###################- - Truy Cập phần tử - -####################
print(infor['name'])
print(infor.get('job'))  # (-> None) nếu key truy cập không có trong dictionary

a = list(infor.values())
b = list(infor.keys())
c = list(infor.items())

for key in infor.keys():
    print(key, infor[key])

for x in infor.items():
    print(x[0], x[1])

for key, value in infor.items():
    print(key, value)

for key in infor:
    print(key, infor[key])

print(a)
print(b)
print(c)

#####################-- Thêm key : value vào dict --#################
infor = {
    'name' : 'Khương',
    'job' : 'student',
    'city' : 'Ha noi',
    'age' : 20.5
}

infor['web'] = '28tech.com.vn'
print(infor)

infor['name'] = 'Minh'
print(infor)

########################-- Xoa -- ########################
infor = {
    'name' : 'Khương',
    'job' : 'student',
    'city' : 'Ha noi',
    'age' : 20.5
}

infor.pop('name')
print(infor)

del infor['age']
print(infor)

# xóa phần tử ngẫu nhiên bằng popitem()
infor.popitem()
print(infor)

infor.clear()
print(infor)

#############-- Kiểm tra sự tồn tại của key, value --###################
infor = {
    'name' : 'Khương',
    'job' : 'student',
    'city' : 'Ha noi',
    'age' : 20.5
}

print('name' in infor)   #O(1)
print('Ha noi' in infor.values())   # O(n)

###################-- Trộn 2 dict --###########################
a = {
    'name' : 'Khuong',
    'job' : ' dev'
}

b = {
    'web' : '28tech.com.vn',
    'email' : 'kmh@gmail.com'
}

a.update(b)
for x in a:
    print(x, a.get(x))

######################-- dict comprehension --################
a = {1, 2, 3, 4}
d1 = dict()
print(d1)
for x in a:
    d1[x] = x **2
print(d1)

d2 = { x : x**2 for x in a}
print(d2)

s = 'abc'
d = {x : x*3 for x in s}
print(d)

tmp = list(infor.items())
print(tmp)