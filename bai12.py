# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 15:45:24 2024

@author: ADMIN
"""

#Viết một hàm để tạo ra một số nguyên ngẫu nhiên từ 1 đến 1000. Sau đó, kiểm tra xem số đó có phải là số nguyên tố hay không
import random
def question_12():
   n = random.randint(1, 1000)
   if n<1:
      return n,False
   elif n==2:
       return n,True
   elif n>2:
       for i in range(2,n):
           if n%i==0:
               return n,False
           else: 
               return n,True      
print(question_12())
         
    