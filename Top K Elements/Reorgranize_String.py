"""
Given a string, str, rearrange it so that any two adjacent characters are not the same. If such a reorganization of the characters 
is possible, output any possible valid arrangement. Otherwise, return an empty string.

Constraints:  
1 ≤ str.length ≤ 500 
Input string consists of lowercase English letters.
"""

# importing libraries
from collections import Counter
import heapq

# Time Complexity: O(Nlog(26)) = O(N)
# Space Complexity: O(26) = O(1)
def reorganize_string(str):

    # Using counter to create hashmap of frequency of charaters in a string
    map_freq = Counter(str)
    max_heap = []
    
    # Creating max heap to sort
    for char, freq in map_freq.items():
        heapq.heappush(max_heap, (-freq, char))

    result = ""
    prev_freq = 0

    # Popping character having the max frequency and pushing previous character into the heap.
    while max_heap:
        freq, char = heapq.heappop(max_heap)
        
        if prev_freq < 0:
            heapq.heappush(max_heap, (prev_freq, prev_char))
        result = result + char
        freq += 1
        prev_freq, prev_char = freq, char
    if prev_freq < 0:
        return ""
    return result

print(reorganize_string("abb"))