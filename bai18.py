# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 18:08:16 2024

@author: ADMIN
"""

#Viết một hàm để loại bỏ tất cả khoảng trắng thừa trong một chuỗi, bao gồm:
#Loại bỏ khoảng trắng ở đầu và cuối chuỗi.
#Loại bỏ các khoảng trắng dư thừa giữa các từ (chỉ giữ lại một khoảng trắng giữa các từ)
def question_18(s):
    return ' '.join(s.strip().split())
print(question_18("ahihi cái đồ ngốc"))
print(question_18("  ơ Thầy  ganh kìa"))