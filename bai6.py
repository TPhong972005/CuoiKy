# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 20:39:39 2024

@author: ADMIN
"""

#Viết một hàm để tính giai thừa của số nguyên dương n . Giai thừa của n (ký hiệu là n! ) là tích của tất cả các số từ 1 đến n
def question_6(n:int):
    gt=1
    for i in range(1,n+1):
        gt*=i
    return gt
print(question_6(5))        