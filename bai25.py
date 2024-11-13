# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 11:26:53 2024

@author: ADMIN
"""

#Cho một mảng các số nguyên nums đã được sắp xếp theo thứ tự không giảm. Viết một hàm
#để trả về một mảng chứa bình phương của mỗi số trong nums và mảng này cũng phải được
#sắp xếp theo thứ tự không giảm.
def question_25(nums: list[int]):
    # Tính bình phương của mỗi phần tử và lưu vào mảng mới
    binh_phuong = [num ** 2 for num in nums]
    # Sắp xếp lại mảng bình phương theo thứ tự không giảm
    binh_phuong.sort()
    return binh_phuong
nums = [-7, -3, 2, 3, 11]
print(question_25(nums))