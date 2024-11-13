# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 22:50:38 2024

@author: ADMIN
"""

#Viết một hàm để kiểm tra xem một số nguyên nhập vào có lớn hơn một số nguyên cho trước n hay không
def question_19(x: int, n: int):
    if x>n:
        return True
    else:
        return False
x=23
n=32
print(question_19(x,n))
print(question_19(15,5))
print(question_19(2,3))