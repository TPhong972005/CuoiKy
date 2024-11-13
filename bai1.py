# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 19:28:34 2024

@author: ADMIN
"""

#Bạn được cung cấp một số nguyên dương n . Viết một hàm để xác định xem n có phải là số nguyên tố hay không.
def question_1(n):
    if n<1:
       return False
    elif n==2:
        return True
    elif n>2:
        for i in range(2,n):
            if n%i==0:
                return False
            else: 
                return True         
print(question_1(2))
print(question_1(11))