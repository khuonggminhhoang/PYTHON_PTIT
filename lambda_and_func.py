# lambda là một cách định nghĩa hàm vô danh (anonymous),một hàm mà ko cần
# có tên hàm. Nó được sử dunngj khi bạn xây dựng những hàm chỉ bao gồm 
# một câu lệnh , khi đó việc sd keyword def để định nghiwx hà là dư thừa 
# và dài dòng
# lambda parameters : expression

func = lambda x : x**2
print(func(10))
print((lambda x : x**2)(2))

a = [-3,-2, -1, 0, 1, 2]
b = list(filter(lambda x : x % 2 == 0, a))
print(b)

c = list(map(lambda x: x**2, a))
print(c)

sum = lambda x, y, z: x + y + z
print(sum(100, 200, 300))

findmax = lambda x, y : x if x > y else y
print(findmax(100, 200))

print((lambda x : x*2)(10))