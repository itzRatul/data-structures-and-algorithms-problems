'''

Given a binary array, in-place sort it in linear time and constant space. The output should contain all zeroes, followed by all ones.

Input : [1, 0, 1, 0, 1, 0, 0, 1]
Output: [0, 0, 0, 0, 1, 1, 1, 1]

Input : [1, 1]
Output: [1, 1]

'''
from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        zero = 0                          
        for i in nums:                   
            if i == 0:                
                zero += 1                 
        for i in range(len(nums)):       
            if i < zero:                  
                nums[i] = 0                
            else:                         
                nums[i] = 1                
        return nums                     
