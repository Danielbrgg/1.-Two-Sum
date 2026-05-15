from typing import List
"""
nums = [2,7,11,15]
nums = [3,2,4]
nums = [3,3]

target = 9
target = 6
target = 6
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):

            for j in range(i + 1, len(nums)):

                if nums[i] + nums[j] == target:

                    return [i, j]