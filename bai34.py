# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 16:19:41 2024

@author: ADMIN
"""

#Viết một hàm để tìm chuỗi con dài nhất trong chuỗi đầu vào mà không chứa bất kỳ ký tự
#nào bị lặp lại.
def question_34_m(chuoi):
    chuoi_con_dai_nhat = ""
    ds_kt = []
    for char in chuoi:
        if char in ds_kt:
            while ds_kt and ds_kt[0] != char:
                del ds_kt[0]
            del ds_kt[0]
        ds_kt.append(char)
        if len(ds_kt) > len(chuoi_con_dai_nhat):
            chuoi_con_dai_nhat = "".join(ds_kt)
    return len(chuoi_con_dai_nhat)
chuoi = "abcabcbb"
ketqua = question_34_m(chuoi)
print("Chuỗi con dài nhất không chứa ký tự lặp lại là:", ketqua)
def question_34(chuoi):
    chuoi=set(chuoi)
    return len(chuoi)
hi="abcabcdefgh"
print(question_34(hi))