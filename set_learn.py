'''
    set trong python ko theo một trật tự sắp xếp nào cả vì nó theo cấu trúc hashtable
    các phần tử trong set phải là tuple, int, str ... ko được là list vì list có thể bị thay đổi

'''

s = {1,2,3,3,2,1,2,3,1}
s.add('Hoang')
s.add('Minh')
s.add('Khuong')
s.add('b')
s.add('a')
print(s)

a = [7,3,11,19]
b = set(a)
print(b)

# thêm nhiều phần tử vào set, ta dùng hàm update() 
b.update([1, 2, 20])
print(b)

# hợp của set và iterable
ans = b.union(a)
tmp_ans = b | s     # có thể dùng | thay cho hàm union()
print(tmp_ans)
print(ans)
# giao của set và iterable
tmp = b.intersection(s)
tmp_ = b & s        # có thể dùng & thay cho hàm intersection()
print(tmp_)
print(tmp)

# xóa phần tử của set
# pop() xóa phần tử đầu tiên trong set
ans.pop()
print(ans)

# remove(element) xóa element khỏi set s, nếu ko có element trong set in ra thông báo lỗi
ans.add(20)
ans.add(20)
ans.remove(20)
print(ans)

# discard(element) xóa element khỏi set, nếu ko có element trong set ko in ra thông báo lỗi
ans.discard(7)
print(ans)


# clear() xóa hết các phần tử của set
# ans.clear()
# print(ans)

# duyệt set
for x in ans:
    print(x, end=' ')
print()
# toán tử in trong set (O(1)) 
if 2 in ans:
    print('Found')
else:
    print('Not Found')

# hàm s1.difference(s2) : lấy các phần tử thuộc s1, ko thuộc s2 -> set
s1 = {22,12, 24, 76, 88}
s2 = {3, 2, 1, 24, 76, 12}

tmp = s1.difference(s2)
print(tmp)
tmp__ = s1 - s2         # có thể dùng - để biểu thị hàm difference()
print(tmp__)

# s1.symmetric_difference(s2) lấy ra các  phần tử thuộc một trong hai tập, ko lấy phần giao
v = s1.symmetric_difference(s2)
print(v)
v_ = s1 ^ s2
print(v_)

# s1.isdisjoin(s2) xem s1 ko có phần tử chung nào với s2 đúng ko?
s = {'28tech','abc', 'python'}
t = {'28tech', 'python'}
u = {'PTIT', 'BKA', 'UET'}
print(s.isdisjoint(t))
print(s.isdisjoint(u))

# s1.issubset(s2) kiểm tra xem s1 có là con của s2 hay không
print(t.issubset(s))
print(u.issubset(s))

# s1.issuperset(s2) kiểm tra xem s1 có là tập cha của s2 hay không
print(s.issuperset(t))
print(s.issuperset(u))

s = set()
print(type(s))

