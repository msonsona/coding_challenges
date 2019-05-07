# https://leetcode.com/explore/learn/card/array-and-string/201/introduction-to-array/1144/

class Solution:
    # E.g. [1, 7, 3, 6, 5, 6]
    # length = 6
    
    def pivotIndex(self, nums: List[int]) -> int:
        
        length = len(nums)
        
        left_sums = [0] * length
        right_sums = [0] * length
        
        for i in range(length):
            
            previous_index = max(0, i - 1)
            next_index = min(length, i)
            
            left_sums[i] = left_sums[previous_index] + nums[i]
            right_sums[-(i + 1)] = right_sums[-next_index] + nums[-(i + 1)]
            
        for i in range(length):
            
            if left_sums[i] == right_sums[i]:
                return i
            
        return -1