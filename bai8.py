# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 21:38:54 2024

@author: ADMIN
"""

#Viết một hàm để đảo ngược một chuỗi được nhập vào từ bàn phím.
def question_8(n):
    n=str(input("nhâpj gì đi:"))
    return str(n)[::-1]
n="Hello World"
print(question_8(n))