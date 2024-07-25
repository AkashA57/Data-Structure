"""
You are given a sorted array of integers, nums, and two integers, target and k. Your task is to return k number of integers that 
are close to the target value, target. The integers in the output array should be in a sorted order.  
An integer, nums[i], is considered to be closer to target, as compared to nums[j] when |nums[i] - target| < |nums[j] - target|. 
However, when |nums[i] - target| == |nums[j] - target|, the smaller of the two values is selected.

Constraints:  
1 ≤ k ≤ nums.length 
1 ≤ nums.length ≤ 10^3   
nums is sorted in ascending order. 
-10^4 ≤ nums[i], target ≤ 10^4  
"""

from binary_search import binary_search

# Time Complexity: O(logn+k)
# Space Complexity: O(1)
def find_closest_elements(nums, k, target):
    # Handling 3 edge cases where size of the array is equal to result list, target <= first element and target >=last element.
    if len(nums)==k:
        return nums
    if target>=nums[-1]:
        return nums[len(nums)-k:len(nums)]
    if target<=nums[0]:
        return nums[0:k]

    # Doing binary search to find the closest(or second closest on the right hand side) index to the target
    first_index = binary_search(nums, target)
    l_window, r_window = first_index-1, first_index
    # Using sliding window until we find k elements
    while r_window-l_window-1<k:
        if l_window==-1:
            r_window += 1 
        elif r_window==len(nums) or abs(nums[l_window]-target)<=abs(nums[r_window]-target):
            l_window -= 1
        else:
            r_window += 1

    return nums[l_window+1:r_window]