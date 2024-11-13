# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 15:53:14 2024

@author: ADMIN
"""

#Viết một hàm để kiểm tra xem một chuỗi có phải là chữ số hay không. Chuỗi được coi là chữ số nếu tất cả các ký tự trong chuỗi là số và không có ký tự nào khác
def question_14(s:str):
    if s.isdigit():
        return True
    else: 
        return False
print(question_14("ahihi"))
print(question_14("aye123"))
print(question_14("3092"))
