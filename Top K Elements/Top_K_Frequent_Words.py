"""
Given a string array, words, and an integer k, return the k most frequent strings.  Sort the frequencies from highest to lowest and
then return the top k frequent words. Words with the same frequency should be sorted by their lexicographical order.

Constraints:  
1 ≤ words.length ≤ 500 
1 ≤ words[i].length ≤ 10 
words[i] consists of lowercase English letters. 
k is in the range [1, The number of unique words[i]]
"""

from collections import Counter
import heapq

# Time Complexity: O(n+klogn)
# SPace Complexity: O(n+n)=O(n)
def top_k_frequent(words, k):
  
    # Initializing a max_heap and a hashmap that stores frequency of words in an array
    max_heap = []
    freq_counter = Counter(words)

    # Appending words and heapifing after the words are added along with the frequency
    for word, freq in freq_counter.items():
        max_heap.append((-freq, word))
    heapq.heapify(max_heap)
    
    result = []
    # Appending the k top elements from the heap
    for i in range(k):
        result.append(heapq.heappop(max_heap)[1])
        
    return result