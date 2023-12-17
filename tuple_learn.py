"""
    Tuple are ordered
    Accessed by index
    Tuple can contain any sort of object
    Tuple are immutable 
"""
# note: Các phần tử trong tuple ko thể thay đổi
a = (1,2,3)
b = (2804, )
c = ('hi', 2, (2,3), 'A')
print(a)
print(type(a))
print(type(b))
print(type(c))

s = "hoang minh khuong"
tmp = tuple(s)
# print(tmp)
# print(tmp[2:5])
# print(tmp[::-1])
ans = tmp
print(ans)

t = (1, 2, (113, 114, 115), [3,5,7], 'python','java')
print(t[2])
print(type(t[2]))

a, *b = t
print(a, b)
print(type(b))

# duyệt tuple như duyệt list
for x in t:
    print(x)

for i in range(len(t)):
    print(t[i])

# kiểm tra phần tử xuất hiện trong tuple
if 'python' in t:
    print('FOUND')
else:
    print('NOT FOUND')

print('python' in t)

# tuple không thể thay đổi giá trị nhưng nếu item trong tuple
# là object có thể thay đổi được thì bạn vẫn có thể thay đổi các item đó

t[3][0] = 1000
print(t)

# tuple không thể thay đổi nhưng chúng ta có thể xóa nó
del t

# concatenation và repetition:
a = ('hoang', 'minh', 'khuong')
b = ('cqcn05-b', )
c = a + b
print(c)

d = b * 3
print(d)

# sắp xếp tuple
 
a = (4,4,2,6,1,4,7,5,8)
a = tuple(sorted(a))    # sorted(a) trả về list nên phải ép lại kiểu tuple
print(a)

# count(), index()
print(a.count(4))
print(a.index(4))