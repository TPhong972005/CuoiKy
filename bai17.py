# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 17:45:44 2024

@author: ADMIN
"""

#Viết một hàm để tạo ra một danh sách gồm n số nguyên ngẫu nhiên từ 1 đến 100. Sau đó, sắp xếp danh sách theo thứ tự giảm dần.
import random
def question_17(n):
    m = [random.randint(1, 100) for _ in range(n)]
    m.sort(reverse=True)
    return m
print(question_17(20))
