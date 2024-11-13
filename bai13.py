# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 15:39:39 2024

@author: ADMIN
"""

#Viết một hàm để đếm số từ trong một chuỗi. Một từ được định nghĩa là một chuỗi các ký tự không phải khoảng trắng
def question_13(s:str):
    words=s.split()
    return len(words)
s=" Hello  My  name  is  Phong"
print(question_13(s))
print(question_13("chó thành"))

    