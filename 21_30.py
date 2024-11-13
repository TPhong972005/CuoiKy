# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 16:02:31 2024

@author: PC
"""

from typing import Optional, Tuple, List
#21 Tìm hai số trong danh sách có tổng bằng một số nguyên cho trước
def question_21(nums: List[int], target: int) -> Optional[Tuple[int, int]]: 
    ds = {}
    for a in nums:
        socantim = target - a
        if socantim in ds:
            return(socantim, a)
        ds[a] = True
    return None
    
#22 Di chuyển tất cả các số 0 về cuối mảng
def question_22(nums: List[int]) -> None:
    so= 0
    for i in range(len(nums)):
       if nums[i] !=0:
           nums[so], nums[i]= nums[i], nums[so]
           so+=1
    return nums   

#23 Kiểm tra giá trị trùng lặp trong mảng
def question_23(nums: List[int])-> bool:
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            return True
    return False

#24 Tìm phần tử chiếm đa số trong mảng
def question_24(nums: List[int]) -> bool:
    phantu = None
    dem = 0
    for so in nums:
        if dem == 0:
            phantu = so
        dem+=1 if so == phantu else -1
    return phantu

#25 Sắp xếp các bình phương của một mảng đã sắp xếp
def question_25(nums: List[int]) -> List[int]:
    binhphuong=[]
    for i in nums:
        binhphuong.append(i**2)
        binhphuong.sort()
    return binhphuong

#26 Tìm độ dài của chuỗi palindrome dài nhất có thể được tạo ra
import collections
def question_26(s: str) -> int:
    demchuoi= collections.Counter(s)
    length= 0
    for count in demchuoi.values():
        length += count // 2 * 2
        if count % 2 == 1:
            length += 1           
    return length

#27 Tìm chuỗi tiền tố chung dài nhất
def question_27(strs: List[str]) -> str:
    tiento= strs[0]
    for s in strs[1:]:
        while not s.startswith(tiento):
            tiento= tiento[:-1]
            if not tiento:
                return " "
    return tiento
    
#28 Đếm số lần xuất hiện của từng phần tử trong chuỗi
from typing import Dict
def question_28(s: str) -> Dict[str, int]:
    dem={}
    for i in s:
        if i in dem:
            dem[i]+=1
        else:
            dem[i]=1
    return dem

#29 Tìm số trung vị của một danh sách
def question_29(nums: List[int]) -> float:
    nums.sort()
    n=len(nums)
  # Kiểm tra nếu số lượng phần tử là lẻ
    if n%2==1:
        return nums[n//2]
  # Nếu số lượng phần tử là chẵn, tính trung bình cộng của hai giá trị ở giữa
    else:
        giua1= nums[n//2-1]
        giua2= nums[n//2]
    return (giua1+ giua2) / 2

#30 Đếm số lượng từ xuất hiện trong đoạn văn
from typing import Dict
def question_30(paragraph: str) -> Dict[str,int]:
    demtu= paragraph.split()
    dem = {}
    for tu in demtu:
        tu=tu.lower()
        if tu in dem:
            dem[tu] +=1
        else:
            dem[tu] = 1
    return dem





if __name__ == "__main__":
    print(question_21([2,7,11,15], 9))
    print(question_21([1,2,3,4,5], 10))
    print(question_22([0,1,0,3,12]))
    print(question_23([1, 2, 3, 1]))
    print(question_23([1,2,3,4]))
    print(question_23([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
    print(question_24([3, 2, 3]))
    print(question_24([2, 2, 1, 1, 1, 2, 2]))
    print(question_25([-4,-1, 0, 3, 10]))
    print(question_25([-7,-3, 2, 3, 11]))
    print(question_26("abccccdd"))
    print(question_26("a"))
    print(question_26("bb"))        
    print(question_27(["flower", "flow", "flight"]))    
    print(question_27(["dog", "racecar", "car"]))       
    print(question_28("hello"))
    print(question_28("test"))
    print(question_29([1, 3, 4, 2, 5])) 
    print(question_29([1, 2, 3, 4]))        
    print(question_30("apple orange apple banana orange"))     
    print(question_30("hello world hello"))
    
                         