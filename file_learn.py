# open() : hàm để mở file
'''
    các mode mở file:
    r : đọc file
    w : ghi file ( cũng có thể mở file nếu file chưa tồn tại)
    a : mở file để ghi tiếp vào cuối file
    x : tạo file

    thêm đuôi:
     t : nếu là file text
     b : nếu là file nhị phân
'''

import os


if __name__ == '__main__':
    f = open('input.txt', 'rt')
    # print(f.read())
    # đọc tất cả dữ liệu trong file
    # print('-------------')   
    # print(f.read(10))
    # đọc 10 ký tự đầu tiên trong file tính cả \n
    # print(f.readline(), end='')
    # đọc từng dòng kể cả dấu \n cuối dòng
    # for line in f:
    #     print(line, end='')
    # f.close()
    # f = open('input.txt', 'at')
    # f.writelines('hehehe\n')
    # f.close()
    try:
        os.remove('input1.txt')  # xóa file
    except FileNotFoundError :
        print(FileNotFoundError)
    # kiểm tra file tồn tại 
    if os.path.exists('input.txt'):
        print('found')
    else:
        print('not found')