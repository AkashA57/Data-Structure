"""
Given a sorted integer array, nums, and an integer value, target, the array is rotated by some arbitrary number. Search and return 
the index of target in this array. If the target does not exist, return -1.

Constraints:  
All values in nums are unique. 
The values in nums are sorted in ascending order. 
The array may have been rotated by some arbitrary number. 
1 ≤ nums.length ≤ 1000
-10^4 ≤ nums[i]  ≤ 10^4  
-10^4 ≤ target ≤ 10^4  
"""

# Time Complexity: O(logn)
# Space COmplexity: O(1)
def binary_search_rotated(nums, target):
  
  # Replace this placeholder return statement with your code
  left, right = 0, len(nums)-1
  while left<=right:
    mid = (left+right)//2
    if nums[mid]==target:
      return mid
    elif nums[right]<nums[left]:
      if nums[left]>target:
        left += 1
      else:
        right -= 1
    elif nums[right]>=nums[left]:
      if nums[mid]<target:
        left += 1
      else:
        right -= 1

  return -1

print(binary_search_rotated([6,7,1,2,3,4,5], 3))
print(binary_search_rotated([4,5,6,1,2,3], 6))
print(binary_search_rotated([4,5,6,1,2,3],3))
print(binary_search_rotated([4], 1))