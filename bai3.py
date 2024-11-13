# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 20:03:18 2024

@author: ADMIN
"""
#Viết một hàm nhận vào một chuỗi, sau đó đếm và in ra số lượng ký tự viết hoa và ký tự viết thường trong chuỗi đó
def question_3(n:str):
    hoa=0
    thuong=0
    for i in n:
        if i.isupper():
            hoa+=1
        if i.islower():
            thuong+=1
    return hoa,thuong
print(question_3("Hello World"))