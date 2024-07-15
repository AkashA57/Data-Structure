"""
Find the kth largest element in an unsorted array.

Constraints:  
1 ≤ k  ≤ nums.length ≤ 10^3
-10^4 ≤ nums[i] ≤ 10^4  
"""

import heapq

# Time Complexity: O(nlogk)
# Space Complexity: O(k)

def find_kth_largest(nums, k):

    min_heap = []

    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap)>k:
            heapq.heappop(min_heap) 
    return min_heap[0]