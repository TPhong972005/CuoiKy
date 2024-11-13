# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 18:59:23 2024

@author: PC
"""

import random
#11 Viết một hàm để trả về số Fibonacci thứ n
def question_11( n:int) -> int:
    if n<=0:
        return 0
    elif n==1:
        return 1
    else: 
        return question_11(n-1) + question_11(n-2)
    
#12  Viết một hàm để tạo ra một số nguyên ngẫu nhiên từ 1 đến 1000. Sau đó, kiểm tra xem số đó có phải là số nguyên tố hay không.
def question_12(n) -> bool:
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
n= random.randint(1, 1000)
    
#13  Viết một hàm để đếm số từ trong một chuỗi. Một từ được định nghĩa là một chuỗi các ký tự không phải khoảng trắng
def question_13(s: str)-> int:
    tu = s.split()
    return len(tu)

#14  Viết một hàm để kiểm tra xem một chuỗi có phải là chữ số hay không. 
def question_14(s: str) -> bool:
    return s.isdigit()
    
#15  Viết một hàm để kiểm tra xem một biến có giá trị None hay không
def question_15(value) -> bool:
    return value is None

#16 Viết một hàm để tính trung bình cộng, nhận vào số lượng tham số bất kỳ và trả về giá trị trung bình cộng của chúng
def question_16(*arg) -> float:
    if len(arg) == 0:
        return None
    tong= sum(arg)
    dem= len(arg)
    return tong/dem
#17 Viết một hàm để tạo ra một danh sách gồm n số nguyên ngẫu nhiên từ 1 đến 100. Sau đó, sắp xếp danh sách theo thứ tự giảm dần.
def question_17(n: int) -> list:
    dsach=[random.randint(1, 100) for _ in range(n)]
    dsach.sort(reverse= True)
    return dsach

#18 Viết một hàm để loại bỏ tất cả khoảng trắng thừa trong một chuỗi
def question_18( s:str) ->str:
    return ' '.join(s.split())

#19  Viết một hàm để kiểm tra xem một số nguyên nhập vào có lớn hơn một số nguyên cho trước n hay không.
def question_19(x: int, n:int) -> bool:
    if x>n:
        return True
    return False

#20 Viết một hàm yêu cầu người dùng nhập một giá trị từ bàn phím. Nếu người dùng không nhập bất kỳ giá trị nào từ bàn phím (chỉ nhấn Enter), hàm sẽ trả về None
def question_20(a:str) -> str or None:
    if a.strip() == "":
        return None
    return a
    
    
    
    

if __name__ == "__main__":
    print(question_11(10))
    print(n)
    print(question_12(n))
    print(question_13("This is a test."))
    print(question_13("Hello world, how are you?"))
    print(question_14("12345"))
    print(question_14("123a45"))
    print(question_14("0123"))
    print(question_15(None))
    print(question_16())
    print(question_17(3))
    print(question_18("Hello  World"))
    print(question_18("Python  is  fun"))
    print(question_19(5, 10))
    print(question_20("Hello"))
    print(question_20(""))