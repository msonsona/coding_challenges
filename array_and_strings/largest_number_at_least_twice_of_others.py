# https://leetcode.com/explore/learn/card/array-and-string/201/introduction-to-array/1147/

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        # Initialize variables
        max_index = 0
        maximum = 0
        second_max = 0
        
        # Loop over array
        i = 0
        while i < len(nums):
            if nums[i] > maximum:
                # If the current element is greater than the current maximum
                # Update the variables
                second_max = maximum
                maximum = nums[i]
                max_index = i
            elif nums[i] > second_max:
                # Else, if greater than the current second maximum
                # Update just that
                second_max = nums[i]
                
            i += 1
            
        if maximum >= 2 * second_max:
            return max_index
        else:
            return -1