m = int(input())
vobia = bia = m//28
while vobia >= 3 :
    tmp = vobia//3
    bia += tmp
    vobia = vobia%3 + tmp
print(bia)