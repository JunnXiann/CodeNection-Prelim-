
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         dict_nums = {}
#         for i, v in enumerate(nums):
#             print("i :", i)
#             print("v :", v)
#             if v in dict_nums: print( [i, dict_nums[v]] )
#             dict_nums[target - v] = i
#             print(dict_nums)

# nums = [1,3,5,6,7]

# Solution.twoSum(Solution, nums, 11)

import timeit

from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_nums = {}
        for i, v in enumerate(nums):
            if v in dict_nums: return [i, dict_nums[v]]
            dict_nums[target - v] = i
            

nums = [1,3,5,6,7]

Solution.twoSum(Solution, nums, 11)