# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 23:36:07 2024

@author: ADMIN
"""

#Viết một hàm yêu cầu người dùng nhập một giá trị từ bàn phím. Nếu người dùng khôngnhập bất kỳ giá trị nào từ bàn phím (chỉ nhấn Enter), hàm sẽ trả về None
def question_20():
    n=str(input("nhập vào chuoi:"))
    if n=="":
        return None
    else:
        return n
print(question_20())
