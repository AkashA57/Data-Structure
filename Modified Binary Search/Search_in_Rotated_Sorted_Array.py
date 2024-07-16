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
  
  left, right = 0, len(nums)-1
  # Checking until left pointer crosses right
  while left<=right:
    mid = (left+right)//2
    # Condition 1: If the mid value matches the target return mid
    if nums[mid]==target:
      return mid
    # Condition 2: If the left value > mid value, we know the sequence is sorted on the right half
    elif nums[left]>nums[mid]:
      # Condition 2.1: Performing binary search on the sorted half
      if target>nums[mid] and target<=nums[right]:
        left = mid + 1
      # Condition 2.2: If the sorted half doesnot satifies the criteria then checkeing in the unsorted half
      else:
        right = mid - 1
    # Condition 3: If the left value <left mid value, we know the sequence is sorted on the left half
    else:
      # Condition 3.1: Performing binary search on the sorted half
      if target<nums[mid] and target>=nums[left]:
        right = mid - 1
      # Condition 3.2: If the sorted half doesnot satifies the criteria then checkeing in the unsorted half
      else:
        left = mid + 1

  return -1

print(binary_search_rotated([6,7,1,2,3,4,5], 3))
print(binary_search_rotated([4,5,6,1,2,3], 6))
print(binary_search_rotated([4,5,6,1,2,3],3))
print(binary_search_rotated([4], 1))