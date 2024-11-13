# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 21:04:38 2024

@author: ADMIN
"""

#Cho một đoạn văn là một chuỗi ký tự, viết chương trình tìm ra các từ có tỷ lệ xuất hiện lớn
#hơn 20% trong đoạn văn
from collections import Counter
def question_31(paragraph: str, n: int):
    tu=paragraph.split()
    dem_tu={}
    for word in tu:
        if word in dem_tu:
            dem_tu[word]+=1
        else:
            dem_tu[word]=1
    tong_tu=len(tu)
    kq=[]
    for word,count in dem_tu.items():
        if (count/tong_tu)>0.2:
            kq.append(word)
    return kq[:n]
paragraph = "apple apple banana orange orange apple"
n = 2
print(question_31(paragraph,n))