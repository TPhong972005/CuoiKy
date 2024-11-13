# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 15:02:30 2024

@author: ADMIN
"""

def question_10():
    # Nhập chuỗi các số nguyên từ bàn phím, phân cách bởi khoảng trắng
    chuoi = input("Nhập các số nguyên, phân cách bởi khoảng trắng: ").strip()
    #strip có chức năng bỏ khoảng cách đầu cuối
    # Kiểm tra xem chuỗi nhập vào có rỗng hay không
    if not chuoi or chuoi.isalpha():
        return None 
    # Chuyển chuỗi thành danh sách các số nguyên
    danh_sach = list(map(int, chuoi.split()))  
    # Kiểm tra danh sách có rỗng hay không
    if not danh_sach:
        return None
    return danh_sach
hi=[1,1,3,4,1,2]
print(question_10())




    