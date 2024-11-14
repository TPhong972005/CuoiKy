# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 00:19:45 2024

@author: 
"""

#Cho một dãy số nằm trong danh sách, đại diện cho giá của một mặt hàng thay đổi qua từng
#ngày. Viết một hàm để tìm ra lợi nhuận lớn nhất có thể đạt được bằng cách thực hiện một
#lần mua và một lần bán, với điều kiện là phải mua mới được bán
def question_39_m(prices):
    if not prices:
       return 0
    min_price = prices[0]
    max_profit = 0  
    for price in prices:
       min_price = min(min_price, price)  # Cập nhật giá mua thấp nhất
       profit = price - min_price         # Tính lợi nhuận khi bán vào ngày hiện tại
       max_profit = max(max_profit, profit)  # Cập nhật lợi nhuận tối đa

    return max_profit
prices = [6, 7, 8, 9, 20, 5]
gia=[7, 1, 5, 3, 6, 4]
print(question_39_m(prices))
print(question_39_m(gia))