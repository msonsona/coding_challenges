# https://leetcode.com/explore/learn/card/array-and-string/201/introduction-to-array/1148/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = True
        # Iterate over the digits list from the end, adding 1,
        # and bringing front the carry
        i = len(digits) - 1
        
        while i >= 0:
            if carry:
                if digits[i] == 9:
                    digits[i] = 0
                    carry = True
                else:
                    digits[i] += 1
                    carry = False
                    # If we don't need carry, we can even stop looping
                    # as next digits won't change
                    break
            i -= 1
        
        # In the end, if there is carry too, prepend a list with [1]
        # before returning the result
        if carry:
            return [1] + digits
        else:
            return digits
        