from math import *

def menu():
    print('''
        1.Nhập vào số nguyên a, nếu a là số chia hết cho 3 và nằm trong khoảng từ 50 - 100 thì in ra True, ngược lại in ra False
        2.Nhập vào số thực a, kiểm tra xem a có phải là số nguyên hay không, nếu có thì in ra True, ngược lại in ra False
        3.Nhập vào 3 số a, b, c. Tính và in ra d = (a + b)^c Nếu d là số trong khoảng từ 100 - 200 thì in ra True, ngược lại in ra False
        4.Giải phương trình ax^2 + bx + c = 0
        5.Nhập tháng, năm. Hãy cho biết tháng đó có bao nhiêu ngày
        6.Nhập điểm toán, văn, anh. Nếu điểm đúng quy tắc (trong khoảng từ 0 - 10), ta tính điểm trung bình rồi tiến hành xét:
        .Nếu điểm trung bình lớn hơn hoặc bằng 8, toán hoặc văn lớn hơn hoặc bằng 8 và không có điểm nào dưới 6.5 thì in ra “Học sinh giỏi”
        .Nếu không đủ điều kiện học sinh giỏi ta xét nếu điểm trung bình lớn hơn hoặc bằng 6.5, toán hoặc văn lớn hơn hoặc bằng 6.5 và không có điểm nào dưới 5 thì in ra “Học sinh khá”
        .Nếu không đủ điều kiện học sinh khá ta xét nếu điểm trung bình lớn hơn hoặc bằng 5, toán hoặc văn lớn hơn hoặc bằng 5 và không có điểm nào dưới 3.5 thì in ra “Học sinh trung bình”
        .Nếu không đủ điều kiện học sinh trung bình ta xét nếu điểm trung bình lớn hơn hoặc bằng 3.5, toán hoặc văn lớn hơn hoặc bằng 3.5 và không có điểm nào dưới 2 thì in ra “Học sinh yếu”
        .Nếu không đủ điều kiện học sinh yếu ta in ra “Học sinh kém”
        7.Nhập vào n Tính S = 1 + 2 + 3 + 4 + … + n
        8.Nhập vào số nguyên dương a, in toàn bộ ước của a
        9.Nhập vào số nguyên dương a và b, in toàn bộ ước chung của a và b
        10.Dãy số fibonacci là dãy số được định nghĩa như sau: 1, 1, 2, 3, 5, 8, 13,... với số kế tiếp sẽ bằng tổng hai số trước đó Nhập vào A, hãy tìm số trong dãy số fibonacci lớn nhất nhưng không vượt quá A
        11.Nhập vào một dãy số nguyên, ngưng nhập khi người dùng nhập -1. Sau khi nhập xong, in số lớn nhất, số nhỏ nhất trong những số vừa nhập
        12.Một khách sạn có N phòng đôi được đánh số từ 1 đến N và M đoàn khách.
            Với mỗi đoàn khách, ta xếp mỗi cặp khách của đoàn vào một phòng trống theo thứ tự phòng tăng dần.

        .Nếu đoàn khách có số người lẻ thì người khách cuối cùng được xếp vào một phòng trống tiếp theo.

        .Nếu đã hết phòng còn trống thì ta sẽ xếp khách vào những phòng mới chỉ có 1 khách theo thứ tự phòng tăng dần.

        .In ra số khách của mỗi phòng sau khi xếp.

        .Giả sử không có 2 đoàn khách nào đến cùng một lúc.

            Ví dụ 1:
            N = 7, M = 3
            doankhach = [3,7,3]
            Ta in: 2, 2, 2, 2, 2, 1, 2

            Ví dụ 2:
            N = 5, M = 3
            doankhach = [2,3,2]
            Ta in: 2, 2, 1, 2, 0

        13. Một nhà hàng có các món ăn: Gà rán, hamburger, cocacola
            Giá của gà rán là: 30.000đ
            Giá của hamburger là: 25.000đ
            Giá của cocacola là: 10.000đ
        .Yêu cầu người dùng nhập vào số lượng từng món ăn. 
        Sau đó in ra hóa đơn, bao gồm các thông tin tổng tiền của từng món, tổng trước thuế, thuế, tổng sau thuế của tất cả.
        
    ''')

def funct1():
    a = int(input())
    if (a % 3 == 0) and (50 <= a <= 100):
        print('True')
    else:
        print('False')

def funct2():
    a = input()
    if not '.' in a:
        print('True')
    else:
        print('NO')

def funct3():
    a, b, c = map(int, input().split())
    d  = (a + b) ** c
    if 100 <= d <= 200:
        print('True')
    else:
        print('False')
    
def funct4():
    a, b, c = map(int, input().split())
    if a == 0:
        if b == 0:
            print('Vô Nghiệm' if c != 0 else 'Vô Số Nghiệm')
        else:
            print('x =', -c/b)
    else:
        delta = b**2 - 4*a*c
        if delta < 0 :
            print('PT Vô Nghiệm')
        elif delta == 0:
            print('x1 = x2 =', (-b)/(2*a))
        elif delta > 0:
            print('x1 =', (-b + sqrt(delta))/(2*a))
            print('x2 =', (-b - sqrt(delta))/(2*a))

def funct5():
    month, year = map(int, input().split())
    if month == (1 or 3 or 5 or 7 or 8 or 10 or 12):
        print('Số Ngày của tháng', month, ':', 31)
    elif month == (4 or 6 or 9 or 11):
        print('Số Ngày của tháng', month, ':', 30)
    else:
        if (year % 4 == 0 and year % 100 !=0) or (year % 400 == 0):
            print('Số Ngày của tháng', month,':', 29)
        else:
            print('Số Ngày của tháng', month,':', 28)

def funct6():
    math, lit, eng = map(float, input().split())
    if 0 <= (math and lit and eng) <=10:
        avg = (math + lit + eng)/3
        print('Điểm trung bình:',avg)
        if avg >= 8 and (math or lit) >= 8 and (math and lit and eng) >= 6.5:
            print('Học sinh giỏi')
        elif avg >= 6.5 and (math or lit) >= 6.5 and (math and lit and eng) >= 5:
            print('Học sinh khá')
        elif avg >= 5 and (math or lit) >= 5 and (math and lit and eng) >= 3.5:
            print('Học sinh trung bình')
        elif avg >= 3.5 and (math or lit) >= 3.5 and (math and lit and eng) >= 2 :
            print('Học sinh yếu')
        else:
            print('Học sinh kém')

def funct7():
    n = int(input())
    ans = 0
    if n != 0:
        ans = ((n + 1) * n)//2
    print(ans)

def funct8(a):
    ans = []
    for i in range(1, isqrt(a) + 1):
        if a % i == 0:
            ans.append(i)
            if i != a//i:
                ans.append(a//i)
    ans.sort()
    return ans

def funct9():
    a, b = map(int, input().split())
    arr_a = funct8(a)
    arr_b = funct8(b)
    for x in arr_a:
        if x in arr_b:
            print(x, end=' ')
    print()
    
def funct10():
    x = int(input())
    f= [0] * (94)
    f[0] = f[1] = 1
    for i in range(2, 93):
        f[i] = f[i-1] + f[i-2]
    
    l =0; r = 93
    ans = -1
    while(l <= r):
        m = (l + r)//2
        if f[m] <= x:
            ans = m
            l = m + 1
        else:
            r = m - 1
    if ans != -1:
        print(f[ans])

def funct11():
    a = []
    while True:
        x = int(input())
        if x == -1:
            break
        a.append(x)
    a.sort()
    print('min =', a[0])
    print('max =', a[len(a) - 1])
        
def funct12():
    n, m = map(int, input().split())
    cus = list(map(int, input().split()))
    hol =[0] * n
    if 2*n < sum(cus):
        print('không đủ phòng')
    elif 2*n == sum(cus):
        for i in range(n):
            print('2,', end='')
        print()
    else:
        idx = 0
        for x in cus:
            while x != 0:
                if idx >= n:
                    idx = 0
                if x >=2 and hol[idx] == 0:
                    hol[idx] = 2
                    idx += 1
                    x -= 2
                elif x < 2 and hol[idx] != 2:
                    hol[idx] += 1
                    idx += 1
                    x -= 1
                else:
                    idx += 1
        for i in range(n-1):
            print(str(hol[i]) + ',', end='')
        print(hol[n-1])

def funct13():
    print('Lượng Gà rán: ', end='')
    chic = int(input())
    print('Lượng Hamburger: ', end='')
    hamb = int(input())
    print('Lượng Cocacola: ', end='')
    coca = int(input())
    print('\n______Bill_____')
    print('Gà rán:', 30000 * chic)
    print('Hamburger:', 25000 * hamb)
    print('Cocacola:', 10000 * coca)
    sum = 30000 * chic + 25000 * hamb + 10000 * coca
    tax = 0.05 * sum
    sum_in_tax = sum + tax
    print('--------------------')
    print('Tổng tiền:', sum)
    print('Thuế:', tax)
    print('Số tiền phải trả:', sum_in_tax)

if __name__ == '__main__':
    while(True):
        menu()
        print('Nhap lua chon (1 -> 13): ', end=' ')
        select = int(input())
        if select <= 0 or select > 13:
            break
        if select == 1: funct1()
        elif select == 2: funct2()
        elif select == 3: funct3()
        elif select == 4: funct4()
        elif select == 5: funct5()
        elif select == 6: funct6()
        elif select == 7: funct7()
        elif select == 8: 
            x = int(input())
            a = funct8(x)
            for x in a:
                print(x, end=' ')
            print()
        elif select == 9: funct9()
        elif select == 10: funct10()
        elif select == 11: funct11()
        elif select == 12: funct12()
        elif select == 13: funct13()