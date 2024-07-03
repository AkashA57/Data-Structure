"""
Find the kth smallest element in an (nxn) matrix, where each row and column of the matrix is sorted in ascending order. Although 
there can be repeating values in the matrix, each element is considered unique and, therefore, contributes to calculating the  kth 
smallest element.
Constraints:  
n == matrix.length 
n == matrix[i].length 
1 ≤ n ≤ 100 
-10^3 ≤  matrix[i][j] ≤ 10^3   
1 ≤ k ≤ n^2  
"""

from heapq import *

# Time complexity: O(klog(n))
# Space complexity: O(n)
def kth_smallest_element(matrix, k):

    min_heap = []
    counter = 0
    # Adding first element of each rows in a matrix along with its index.
    for i in range(len(matrix)):
        heappush(min_heap, (matrix[i][0], i, 0))

    # Poping and pushing until we pop k elements.
    while counter<k:
        value, ind1, ind2 = heappop(min_heap)
        if ind2+1<len(matrix):
            heappush(min_heap, (matrix[ind1][ind2+1], ind1, ind2+1))
        counter += 1
    return value

print(kth_smallest_element([[2,6,8],[3,7,10],[5,8,11]], 3))
