""" 
Given an infinite stream of integers (sorted or unsorted), nums, design a class to find the kth largest element in a stream.

The class should have the following functions, inputs, and return values:  
Init(nums, k): It takes an array of integers nums and an integer k and initializes the class object. 
Add(value): It takes one integer value, appends it to the stream, and returns the element representing the kth largest element in 
the stream.

Constraints:  
1 ≤ k ≤ 10^3   
0 ≤ nums.length ≤ 10^3   
-10^3 ≤ nums[i] ≤ 10^3  
-10^3 ≤ value ≤ 10^3  
At most, 10^3 calls will be made to add. 
It is guaranteed that there will be at least k elements in the array when you search for the kth element.
"""

import heapq

# Time complexity: Init: O(nlogk) Add: O(logk)
# Space complexity: k
class Kth_Largest_Element_in_a_Stream:
    # Constructor to initialize heap and add values in it
    def __init__(self, k, nums):
        self.min_heap = []
        self.k = k
        for val in nums:
            self.add(val)

    # Adds element in the heap and return the Kth largest
    def add(self, val):
        # Adding k items in a heap
        if len(self.min_heap)<self.k:
            heapq.heappush(self.min_heap, val) 
        # Popping the root and adding new value if new value is larger than the root
        elif val>self.min_heap[0]:
            heapq.heappop(self.min_heap)
            heapq.heappush(self.min_heap, val)
        return self.min_heap[0]