# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 10:05:00 2024

@author: ADMIN
"""

#Viết một hàm nhận vào một mảng các số nguyên nums . Trả về True nếu có bất kỳ giá trị
#nào xuất hiện ít nhất hai lần trong mảng, và trả về False nếu tất cả các phần tử trong mảng
#đều khác nhau
def question_23(nums: list[int]):
    socotontairoi=set()
    for num in nums:
        if num in socotontairoi:
            return True
        socotontairoi.add(num)#chức năng dòng này trả số lại từ set vào lại nums nếu dò hết mà vẫn không có thì nums vẫn giữ nguyên.
    return False
        
nums = [1, 2, 3, 5, 2]
print( question_23(nums))