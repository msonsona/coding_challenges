# https://leetcode.com/explore/interview/card/facebook/5/round-1-phone-interview/262/
class Solution:
    def moveZeroes(self, nums): # moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        num_iterations = 0
        nums_length = len(nums)
        while num_iterations < nums_length:
            # print(f"{nums} At position {i}, we have {nums[i]}")
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
            else:
                i += 1
            num_iterations += 1
            # print(nums)
