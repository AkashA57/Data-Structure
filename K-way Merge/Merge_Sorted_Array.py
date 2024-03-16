"""
Given two sorted integer arrays, nums1 and nums2 , and the number of data elements in each array, m and n, implement a function that
merges the second array into the first one. You have to modify nums1 in place. 
Note: Assume that nums1 has a size equal to m+n , meaning it has enough space to hold additional elements from nums2.
Constraints:
nums1.length = m+n
nums2.length = n 
0 ≤ m,n ≤ 200
1 ≤ m+n ≤ 200
-10^3 ≤ nums1[i], nums2[j] ≤ 10^3
"""

# Time complexity O(m+n). Space complexity O(1)
def merge_sorted(nums1, m, nums2, n):

    # Here, p and p2 points to the end of the nums1 and nums2 array. p1 points to the end of the nums1 array where data elements are filled.
    p = len(nums1)-1
    p1 = m-1
    p2 = n-1

    # We start looping from end to first and start populating the largest value 
    while p>-1:
        if p1>-1 and (p2<0 or nums1[p1]>nums2[p2]):
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1
    return nums1

print(merge_sorted([6,7,8,9,10,0,0,0,0,0] , 5 , [1,2,3,4,5] , 5))

"""
Course solution
"""
# def merge_sorted(nums1, m, nums2, n):
#     p1 = m - 1  
#     p2 = n - 1 
#     for p in range(n + m - 1, -1, -1):
#    # We can break the loop if we populate all the elemnts from nums2 to the nums1 array.
#         if p2 < 0:
#             break
#         if p1 >= 0 and nums1[p1] > nums2[p2]:
#             nums1[p] = nums1[p1]
#             p1 -= 1
#         else:
#             nums1[p] = nums2[p2]
#             p2 -= 1
#     return nums1