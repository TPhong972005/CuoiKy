# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 18:17:02 2024

@author: ADMIN
"""

def question_35_m(chuoi):
    chuoi_con_dai_nhat = ""
    n = len(chuoi)
    for i in range(1, n // 2 + 1):
        chuoi_con_da_gap = set()
        for m in range(n - i + 1):
            chuoi_con = chuoi[m:m + i]
            if chuoi_con in chuoi_con_da_gap:
                if len(chuoi_con) > len(chuoi_con_dai_nhat):
                    chuoi_con_dai_nhat = chuoi_con
            else:
                chuoi_con_da_gap.add(chuoi_con)
    return chuoi_con_dai_nhat
chuoi = "aabcdeaabcd"
ketqua = question_35_m(chuoi)
print("Chuỗi con lặp lại dài nhất là:", ketqua)