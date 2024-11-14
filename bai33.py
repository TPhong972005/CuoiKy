# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 16:06:08 2024

@author: ADMIN
"""
#Cho một danh sách nums chứa các số nguyên. Viết một hàm để tìm phần tử lớn thứ 2 và
#phần tử nhỏ thứ 5 trong danh sách
def question_33_m(so):
    ds_moi = list(set(ds))
    ds_moi.sort()
    print(ds_moi)
    if len(ds_moi) < 2:
        so_lon_thu_2 = None
    else:
        so_lon_thu_2 = ds_moi[-2]
    if len(ds_moi) < 5:
        so_be_thu_5 = None
    else:
        so_be_thu_5 = ds_moi[3]
    return so_lon_thu_2, so_be_thu_5

ds = [3, 1, 4, 5, 9, 2, 6, 8, 7]
print(question_33_m(ds))