# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 19:48:48 2024

@author: ADMIN
"""

#Viết một hàm tạo ra n số nguyên ngẫu nhiên từ 1 đến 100. Sau đó, tính tổng và trung bình của các số này
import random
def question_2(n):
    m = [random.randint(1, 100) for _ in range(n)]
    tong=sum(m)
    tb=tong/n
    return "tong",tong,"trungbinh",tb
print(question_2(5))