a = [1,2,3,4,5]

b = [x * 2 for x in a]
print(b)

c = [x for x in a if x > 3]
print(c)

a = [[1,2,3], [4,5], [6,7,8,9]]
b = [x for small_list in a for x in small_list]
print(b)