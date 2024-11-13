# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 19:59:01 2024

@author: ADMIN
"""

#Số trung vị của một danh sách các số nguyên là giá trị ở vị trí giữa khi danh sách được sắp
#xếp theo thứ tự tăng dần. Nếu danh sách có số lượng phần tử là lẻ, số trung vị là giá trị
#giữa. Nếu danh sách có số lượng phần tử là chẵn, số trung vị là trung bình cộng của hai giá
#trị ở giữa
def question_29(nums):
    # Sắp xếp danh sách các số
    nums.sort()
    
    n = len(nums)
    
    # Nếu số lượng phần tử là lẻ, trả về giá trị giữa
    if n % 2 != 0:
        return nums[n // 2]
    # Nếu số lượng phần tử là chẵn, trả về trung bình cộng của hai giá trị giữa
    else:
        mid1 = nums[n // 2 - 1]
        mid2 = nums[n // 2]
        return (mid1 + mid2) / 2
hihi=[1,2,3,4,5,6]
giua=hihi[len(hihi)//2]
print(giua)
#khovl
nums = [1, 2, 3, 4]
print(question_29(nums))
print(question_29(hihi))
