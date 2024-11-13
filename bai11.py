# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 15:02:39 2024

@author: ADMIN
"""

#Viết một hàm question_11(n) để trả về số Fibonacci thứ n . Dãy số Fibonacci được định nghĩa như sau:
def question_11(n: int):
    # Kiểm tra nếu n là số 0 hoặc 1, trả về n vì F(0) = 0, F(1) = 1
    if n <= 1:
        return n   
    # Khởi tạo hai số Fibonacci đầu tiên
    a, b = 0, 1   
    # Tính các số Fibonacci từ 2 đến n
    for _ in range(2, n + 1):
        a,b=b,a+b
    return b    
print(question_11(3))

