# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 07:06:03 2024

@author: ADMIN
"""

#26 Tìm độ dài của chuỗi palindrome dài nhất có thể được tạo ra
import collections
def question_26(s: str) -> int:
    demchuoi= collections.Counter(s)
    length= 0
    for count in demchuoi.values():
        length += count // 2 * 2
        if count % 2 == 1:
            length += 1           
    return length
s="abbccdd"
print(question_26(s))