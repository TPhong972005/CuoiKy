# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 09:24:10 2024

@author: ADMIN
"""

def question_21(nums: list[int], target: int):
  # Sử dụng một tập hợp để lưu các số đã duyệt qua
   
    
    # Duyệt qua từng số trong danh sách
    for num in nums:
        # Tính số còn thiếu cần để đạt được tổng target
        complement = target - num
        
        # Kiểm tra nếu số còn thiếu đã tồn tại trong tập hợp
        if complement in nums:
            return (complement, num)
        
        # Nếu chưa, thêm số hiện tại vào tập hợp
        
    
    # Nếu không tìm thấy cặp số nào, trả về None
    return None
nums = [2, 7, 11, 15]
target = 18
print(question_21(nums,target))  