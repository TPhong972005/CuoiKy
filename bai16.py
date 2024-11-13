# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 17:29:15 2024

@author: ADMIN
"""

#Viết một hàm để tính trung bình cộng, nhận vào số lượng tham số bất kỳ và trả về giá trị trung bình cộng của chúng.
def question_16(*args):
    if len(args)==0:
        return 0
#độ dài bằng 0 k có chứ số nào
    return sum(args)/len(args)
#sum tính tổng các số
#len tính có bao nhiêu chữ 
print(question_16(1,3,5,6,9))
print(question_16(2,9,0,3))
    