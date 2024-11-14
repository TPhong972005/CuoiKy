# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 16:02:52 2024

@author: ADMIN
"""
#Cho một danh sách các số nguyên nums , phân chia danh sách thành hai danh sách:
#1. Danh sách các số chẵn, được sắp xếp theo thứ tự giảm dần (từ lớn đến nhỏ).
#2. Danh sách các số lẻ, được sắp xếp theo thứ tự tăng dần (từ nhỏ đến lớn)
def question_32_m(ds):
    ds_moi = sorted(ds, reverse= False)
    chan = []
    le = []
    for i in ds_moi:
        if i % 2 == 0:
            chan.append(i)
        else:
            le.append(i)
    capchan = tuple(chan)
    capchan = sorted(capchan, reverse= True)
    caple = tuple(le)
    caple = sorted(caple, reverse= False)
    return capchan, caple
so = input("Nhập vào danh sách các số, cách nhau bởi dấu phẩy: ")
ds = [int(num.strip()) for num in so.split(",") if num.strip()]
print(question_32_m(ds))