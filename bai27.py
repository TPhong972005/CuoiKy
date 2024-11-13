# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 20:28:37 2024

@author: ADMIN
"""

#Viết một hàm để tìm chuỗi tiền tố chung dài nhất trong một mảng các chuỗi. Nếu không có
#tiền tố chung, trả về một chuỗi rỗng "" .
def question_27(strs: list[str]):
    if not strs:
        return ""

    # Bắt đầu với tiền tố là chuỗi đầu tiên
    prefix = strs[0]

    # Duyệt qua các chuỗi còn lại trong mảng
    for s in strs[1:]:
        # Cắt tiền tố cho đến khi nó là tiền tố của chuỗi hiện tại
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            # Nếu tiền tố trở thành chuỗi rỗng, không có tiền tố chung
            if not prefix:
                return ""
    
    return prefix
strs = ["flower", "flow", "flight"]
print(strs[1:])
print(strs[:-1])
print(question_27(strs))