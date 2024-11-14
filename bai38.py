# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 23:06:14 2024

@author: Tphong
"""
#Giả sử bạn đang đứng trước cầu thang có n bậc thang. Mỗi lần bạn có thể bước lên 1 bậc
#hoặc 2 bậc. Viết một hàm để tính số cách bạn có thể leo hết bậc thang
import random 
def question_38_m(n):
    if n <= 2:
        return n

    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b

    return b
print(question_38_m(5))
print(question_38_m(2))
print(question_38_m(3))