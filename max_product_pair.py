'''

Given an integer array, find a pair with the maximum product in it.

Each input can have multiple solutions. The output should match with either one of them.

Input : [-10, -3, 5, 6, -2]
Output: (-10, -3) or (-3, -10) or (5, 6) or (6, 5)

Input : [-4, 3, 2, 7, -5]
Output: (3, 7) or (7, 3)

If no pair exists, the solution should return an empty tuple.

Input : [1]
Output: ()

'''
from typing import List, Tuple
class Solution:
	def findPair(self, nums: List[int]) -> Tuple[int]:

		if len(nums) < 2 :
			return () 
		nums.sort()
		a = nums[0] * nums[1] 

		b=nums[len(nums)-1]*nums[len(nums)-2]
		if a>b :
			return (nums[0],nums[1])
		else :
			return (nums[len(nums)-1],nums[len(nums)-2])
		

