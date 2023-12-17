# replace()
s = "28tech,,,python,,,,,C++"
t = s.replace('python', 'java')
a = s.replace(',',' ').split()
print(a)

#join(): kết hợp các từ rời rạc thành một xâu được phân cách bởi kí tự cho trước
a = ['28tech', 'python', 'C++']
s = ' '.join(a)
print(s)

# các hàm case conversion:
'''
    upper()
    lower()
    capitalize(): viết hoa chữ cái đầu của xâu, các kí tự còn lại in thường
    swapcase() : viết chữ hoa thành chữ thường và ngược lại
    title(): Viết hoa các chữ cái đầu của từng từ, các ký tự còn lại viết thường

'''
s = "hoAnG MinH hehe,KhuoNG"
s1 = s.upper()
print(s1)
s2 = s.lower()
print(s2)
s3 = s.capitalize()
print(s3)
s4 = s.swapcase()
print(s4)
s5 = s.title()
print(s5)

# dùng in hoặc find() để kiểm tra xâu con
s = "28tech,,,python,,,,,C++"
if '28tech' in s:
    print('FOUND')
# find() trả về chỉ số đầu tiên của xâu con xuất hiện trong str
print(s.find('28tech'))
print(s.find('no'))

# ascii -> kí tự và ngc lại
print(ord('A'))
print(chr(65))