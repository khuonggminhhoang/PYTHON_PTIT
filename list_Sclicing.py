# a[start : stop : step]

a = [10, 20, 30, 40, 50, 60, 70, 80, 90]
b = a[2:5:1]
print(b)

c = a[::-1]
print(c)

# chèn và xóa với list slicing

print(a)
a[2:5] = [1, 2, 3, 4, 5]  
# a[2 : 5 : 1] = [1, 2, 3, 4, 5]  
print(a)

# chèn đầu
a[:0] = [9, 8, 7]
print(a)

# chèn cuối
a[len(a) : ] = ['x', 'y', 'z']
print(a)

# xoa 1 đoạn list
a[:3] = []
print(a)