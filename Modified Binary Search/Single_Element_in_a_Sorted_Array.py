"""
You are given a sorted array of integers, nums, where all integers appear twice except for one. Your task is to find and return the
single integer that appears only once. 
The solution should have a time complexity of O(logn) or better and a space complexity of O(1) .

Constraints:  
1 ≤ nums.length ≤ 10^3   
0 ≤ nums[i] ≤ 10^3  
"""

# Time Complexity: O(logn)
# Space Complexity: O(1)
def single_non_duplicate(nums): 

  # Initializing two pointers for a binary search 
  left, right = 0, len(nums)-1
  # When left equals right, then we have found our unique number   
  while left!=right:
    mid = (left+right)//2
    if mid%2==1:
      mid -= 1
    # Since the numbers are in pair, we can say that if mid is even, then element at mid and mid+1 is equal.
    if nums[mid]==nums[mid+1]:
      left = mid+2
    # Otherwise, the unique element lies at the left of the mid, inclusive.
    else:
      right = mid
  return nums[left]