# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 20:26:15 2024

@author: ADMIN
"""

#Viết một hàm để tìm phần tử x trong một danh sách lst . Nếu tìm thấy, trả về vị trí (chỉ số) của phần tử đó, nếu không, trả về None .
def question_5(lst:list,x:int):
    dem=0
    if x in lst:
       return lst.index(x)
lst=[1, 2, 3, 4, 5]
print(question_5(lst,3))
