"""
Given an m number of sorted lists in ascending order and an integer, k, find the k th smallest number among all the given lists. 
Although there can be repeating values in the lists, each element is considered unique and, therefore, contributes to calculating 
the k th smallest element. If k is greater than the total number of elements in the input lists, return the greatest element from 
all the lists, and if there are no elements in the input lists, return 0.

Constraints:
1 ≤ m ≤ 300
0 ≤ list[i].length ≤ 300
-10^9 ≤ list[i][j] ≤ 10^9
1 ≤ k ≤ 10^9
"""

from heapq import *

# Time complexity: O((m+k)logm)
# Space complexity: O(m)
def k_smallest_number(lists, k):

    # Storing the first element from all the sorted list in the array to a min heap
    min_heap = []
    for i in range(len(lists)):
        if len(lists[i])>0:
            heappush(min_heap, (lists[i][0], i, 1))
    
    min_num = 0
    counter = 0

    # Counting the nth smallest num and storing it's value by popping from min_heap.
    # If popped item has the next element in the list we add it to the min_heap.
    while min_heap:
        min_num, list_i, item_no = heappop(min_heap)
        counter += 1
        if counter==k:
            break
        if item_no<len(lists[list_i]):
            heappush(min_heap, (lists[list_i][item_no], list_i, item_no+1))
    return min_num