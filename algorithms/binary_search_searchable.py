#!/bin/python3

# Return the number of searchable elements in the binary tree
# represented as an array in arr
def numSearchable(arr):
    # Initialize the valid ranges of nodes to None
    # We'll update them as we traverse the tree from root to leaves
    valid_range = [{'min': None, 'max': None} for _ in range(len(arr))]

    num_searchable_elems = 0
    for i in range(len(arr)):
        if i == 0:
            valid_range[i]['min'] = float('-inf') # Negative infinity
            valid_range[i]['max'] = float('inf') # Positive infinity
            num_searchable_elems += 1
        else: 
            # Compute parent of current node
            parent_i = (i - 1) // 2

            # Update the range given parent range and value
            if i % 2 == 0: 
                # Current node is a right child
                # => so restrict the min valid value
                valid_range[i]['min'] = max(valid_range[parent_i]['min'], arr[parent_i])
                valid_range[i]['max'] = valid_range[parent_i]['max']

            else: 
                # Current node is a left child
                # => so restrict the max valid value
                valid_range[i]['min'] = valid_range[parent_i]['min']
                valid_range[i]['max'] = min(valid_range[parent_i]['max'], arr[parent_i])

            # Then check current value within range
            if arr[i] > valid_range[i]['min'] and arr[i] < valid_range[i]['max']:
                num_searchable_elems += 1

    return num_searchable_elems

if __name__ == '__main__':
    arr = [17,12,35,5,15,24,43]
    print(numSearchable(arr)) # => 7

    arr = [17,19,35,5,15,24,43] # 19 and 15 aren't searchable
    print(numSearchable(arr)) # => 5
