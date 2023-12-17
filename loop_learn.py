for i in range(1,11,1):
    print(i, end = " ")
else : print("not print")


# for var in range(start, stop, step) : 
# code....
# else : ....

for i in range(5):
    print(i)
    i+=1

for i in range(1, 10, 3):
    print(i, end= " ")


# break and continue
a = 20; b = 100
for i in range(a, b+1):
    if i % 2 == 0: continue
    print(i, end= ' ')
    if i == 61: break
print()

# while loop:
i = 1
while i <= 5 :
    print(i)
    i+=1
else :              
    print("vong lap while ket thuc")
print("cac cau lenh ben duoi")