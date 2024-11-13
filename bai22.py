# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 09:41:08 2024

@author: ADMIN
"""

#Viết một hàm nhận vào một mảng các số nguyên nums . Di chuyển tất cả các số 0 trong
#mảng về cuối mảng trong khi vẫn giữ nguyên thứ tự của các phần tử không phải số 0.
def question_22(nums: list[int]):
    index = 0

    # Duyệt qua mảng, đưa các phần tử không phải số 0 lên đầu
    for num in nums:
        if num != 0:
            nums[index] = num
            index += 1

    # Sau khi các phần tử không phải số 0 đã được di chuyển lên đầu,
    # gán các phần tử còn lại (từ vị trí index trở đi) thành 0
    for i in range(index, len(nums)):
        nums[i] = 0

    return nums
nums=[0,2,9,0,3,2,4,5]
print(question_22(nums))