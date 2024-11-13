# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 19:21:21 2024

@author: ADMIN
"""

#Viết một hàm để đếm số lần xuất hiện của từng phần tử (ký tự) trong một chuỗi. Trả về kết
#quả dưới dạng một từ điển, trong đó các khóa là các ký tự và giá trị là số lần xuất hiện của
#ký tự đó.
def question_28(s: str):
    dem={}
    for char in s:
        if char in dem:
            dem[char] += 1
        else:
            dem[char] = 1
    return dem

from collections import Counter

def question_28s(s: str):
    return dict(Counter(s))

s = "hello"
print(question_28s(s))
print(question_28(s))