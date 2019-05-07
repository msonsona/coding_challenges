# https://leetcode.com/explore/learn/card/array-and-string/202/introduction-to-2d-array/1167/

class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        
        if len(matrix) == 0:
            return []
        
        direction = "NE" # direction will be one of ["NE", "SW"]
        
        i = 0
        j = 0
        M = len(matrix)
        N = len(matrix[0])
        
        elements = [None] * M * N
        elem_index = 0
        
        while 0 <= i and i < M and 0 <= j and j < N:
            elements[elem_index] = matrix[i][j] # Collect the current element
            
            if direction == "NE":
                if i == 0: # We're at the top border, so change direction
                    direction = "SW"
                    if j < N - 1: # Move right if we can
                        j += 1
                    else: # If not, we'll move down
                        i += 1
                elif j == N - 1: # We're at the right border
                    direction = "SW"
                    i += 1
                else: # Just move along normally
                    i -= 1
                    j += 1
                
            else: # direction == "SW"
                if j == 0: # We're at the left border
                    direction = "NE"
                    if i < M - 1: # Move down if we can
                        i += 1
                    else: # If not, we'll move right
                        j += 1 
                elif i == M - 1: # We're at the bottom border
                    direction = "NE"
                    j += 1
                else: # Just move along normally
                    i += 1
                    j -= 1
    
            elem_index += 1
                    
        return elements
                
        