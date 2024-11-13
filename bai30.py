# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 20:17:49 2024

@author: ADMIN
"""

#Cho một đoạn văn là một chuỗi ký tự, viết chương trình đếm số lượng mỗi từ xuất hiện
#trong đoạn văn đó.
from collections import Counter
def question_30(paragraph: str):
    tu = paragraph.split()
    dem=Counter(tu)
    return dict(dem)
paragraph = "Hello! I love u so much"
print(question_30(paragraph))