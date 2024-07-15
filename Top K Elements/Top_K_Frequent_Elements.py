from heapq import heappush, heappop
from collections import Counter

# Time complexity: O(nlogk)
# Space complexity: O(n)
def top_k_frequent(arr, k):

    # Initiliazing min heap and hashmap that contains frequency using counter module
    min_heap = []
    int_freq = Counter(arr)

    # Iterating through hashmap and pushing elements in the heap while popping if elements exceed k.
    for element, freq in int_freq.items():
        heappush(min_heap, [freq, element])
        if len(min_heap)>k:
            heappop(min_heap)
    result = []

    # Extracting the elements while discounting frequency for the final result list
    for x in min_heap:
        result.append(x[1])
    return result