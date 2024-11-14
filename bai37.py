# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 18:45:30 2024

@author: ADMIN
"""
#Cho một chuỗi s chỉ chứa các ký tự '(', ')', '{', '}', '[' và ']'. Viết một hàm để xác định xem
#chuỗi đầu vào có hợp lệ hay không
def question_37(chuoi: str):
    chuoi_kt = []
    cap = {')': '(', '}': '{', ']': '['}
    for char in chuoi:
        if char in cap:
           if not chuoi_kt:
               return False
           kt_dau = chuoi_kt[-1]
           if cap[char] != kt_dau:
               return False
           chuoi_kt = chuoi_kt[:-1]
        else:
           chuoi_kt.append(char)
    return not chuoi_kt
#chuoi = inp)ut("Nhập vào chuỗi kí tự: ")
s = "([()])"
q="()()[]"
print(s[:-1])
print(question_37(s))
print(question_37(q))