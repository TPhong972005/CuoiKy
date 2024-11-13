# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 18:45:37 2024

@author: ADMIN
"""

#Viết một hàm nhận vào một mảng số nguyên nums có kích thước n . Trả về phần tử chiếm
#đa số trong mảng. Phần tử chiếm đa số là phần tử xuất hiện nhiều hơn [n / 2] lần. Bạn có
#thể giả định rằng phần tử chiếm đa số luôn tồn tại trong mảng.
from collections import Counter

def question_24(nums: list[int]) -> int:
    # Đếm số lần xuất hiện của từng phần tử
    counts = Counter(nums)
    # Trả về phần tử có tần suất lớn hơn n / 2
    return max(counts, key=counts.get)
nums=[3, 2, 3,4,5,4,4,5,4]
print(question_24(nums))