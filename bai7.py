# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 20:42:55 2024

@author: ADMIN
"""

#Viết một hàm tạo ra n số thực ngẫu nhiên trong khoảng từ 0 đến 1. Sau đó, tìm số lớn nhất và số nhỏ nhất trong danh sách đó.
import random
def question_7(n: float):
    m =[random.random() for _ in range(n)]
    ln=round(max(m),4)
    nn=round(min(m),4)
    return ln,nn
print(question_7(5))