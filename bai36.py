# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 12:35:39 2024

@author: ADMIN
"""
from itertools import permutations
def question_36(nums):
    return [list(p) for p in permutations(nums)]
#học hàm nếu nhớ
nums=[1,2,3]
def question_36_m(so):
    def tao_hoanvi(hientai, dao):
        if not dao:
            ketqua.append(hientai)
        for i in range(len(dao)):
            tao_hoanvi(hientai + [dao[i]], dao[:i] + dao[i + 1:])
    ketqua = []
    tao_hoanvi([], nums)
    return ketqua
print(question_36(nums))
print(question_36_m(nums))
