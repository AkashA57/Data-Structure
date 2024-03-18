"""
Given two lists, and an integer k , find k pairs of numbers with the smallest sum so that in each pair, each list contributes one 
number to the pair.
Constraints: 
1 ≤ list1.length, list2.length ≤ 500 
-10^4 ≤ list1[i], list2[i] ≤ 10^4
1 ≤ k ≤ 10^3 
Input lists should be sorted in ascending order. 
If the value of k exceeds the total number of valid pairs that may be formed, return all the pairs.
"""

from heapq import *

# Time complexity: O(klogm), where m is the minimum of k and list1.
# Space complexity: O(m)
def k_smallest_pairs(list1, list2, k):

    result = []
    sum_mheap = []
    # Storing minimum of k and list1 pairs in min heap along with their sum and indexes.
    for i in range(min(k, len(list1))):
        heappush(sum_mheap, (list1[i]+list2[0], i, 0))

    counter = 0
    # Popping smallest sum and adding the pairs to the result k times while incrementing index of list2 and adding to the min heap.
    while sum_mheap and counter<k:
        min_sum, l1_ind, l2_ind = heappop(sum_mheap)
        result.append((list1[l1_ind], list2[l2_ind]))
        
        if l2_ind+1<len(list2):
            heappush(sum_mheap, (list1[l1_ind]+list2[l2_ind+1], l1_ind, l2_ind+1))
        
        counter += 1
    return result


print(k_smallest_pairs([1,2,300], [1,11,20,35,300], 30))
