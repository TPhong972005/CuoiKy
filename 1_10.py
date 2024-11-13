# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 20:02:07 2024

@author: PC
"""

import random
#1 số nguyên tố
def question_1(n:int) -> bool:
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

#2 số nguyên ngẫu nhiên và tính tổng, trung bình
def question_2(n: int) -> (int, float):
    songaunhien= [random.randint(1, 100) for _ in range(n)]
    tong = 0
    for so in songaunhien:
        tong+=so
    if n>0:
        tbinh = tong/n
    else:
        return False
    return songaunhien, tong, tbinh
    n = songaunhien, tong, tbinh
    
#3 đếm ký tự viết hoa và viết thường
def question_3 (s:str) -> (int,int):
    chu_hoa = 0
    chu_thuong = 0
    for chuoi in s:
        if chuoi.isupper():
            chu_hoa +=1
        elif chuoi.islower():
            chu_thuong +=1
    return chu_hoa, chu_thuong

#4 Kiểm tra số chẵn
def question_4 (n: int) -> bool:
    for i in range(1,n+1):
        if n%2==0:
            return True
        else:
            return False
    
#5 Tìm phần tử trong danh sách
def question_5(lst: list, x:int) -> int or None:
    if x in lst:
        return lst.index(x)
    return None

#6 Tính giai thừa của một số nguyên dương
def question_6(n: int) -> int:
    giaithua=1
    for i in range(1,n+1):
        giaithua *=i
    return giaithua

#7  Tạo danh sách n số thực ngẫu nhiên và tìm số lớn nhất, nhỏ nhất
def question_7 (n: int) -> (float, float):
    thucngau = [random.uniform(0, 1) for _ in range(n)]
    solon = max(thucngau)
    sonho = min(thucngau)
    return thucngau, solon, sonho

#8 Viết một hàm để đảo ngược một chuỗi được nhập vào từ bàn phím
def question_8(s) -> str:
    return s[::-1]

#9 Viết một hàm để kiểm tra xem một chuỗi có phải là chuỗi palindrome hay không.
def question_9(s: str) -> bool:
    s = ''.join(char for char in s if char.isalnum())
    s = s.lower()
    return s == s[::-1]

#10 Viết một hàm nhập vào một danh sách số nguyên từ bàn phím các số nguyên này được phân cách bằng khoảng trắng và trả về None nếu danh sách đó trống.
def question_10(so) -> None:
    if so is None:
        nhapchuoi= input ("Nhập các số nguyên (cách nhau bởi khoảng trắng")
        so= nhapchuoi.split()
        so= [int(num) for num in so]
    if so:
        return so
    else:
        return None
 

    
if __name__ == "__main__":
    print(question_1(2))
    print(question_2(10))
    print(question_3("Hello World"))
    print(question_3("Python Programming"))
    print(question_4(4))
    print(question_4(7))
    print(question_5(lst=[1,2,3,4,5],x=3))
    print(question_5(lst=[10,20,30,40],x=25))
    print(question_6(5))
    print(question_7(5))
    print(question_8("Hello World"))
    print(question_9("A man, a plan, a canal: Panama"))
    print(question_10([1,2,3]))
    print(question_10([]))
  