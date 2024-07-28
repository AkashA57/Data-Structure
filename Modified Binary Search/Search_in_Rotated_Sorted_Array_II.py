"""
You are required to find an integer t in an array arr of non-distinct integers. Prior to being passed as input to your search 
function, arr has been processed as follows:  
    It has been sorted in non-descending order. 
    It has been rotated around some pivot k, such that, after rotation, it looks like this: [nums[k], nums[k+1], ..., nums[n-1], 
    nums[0], nums[1], ..., nums[k-1]]. For example, [10, 30, 40, 42, 42, 47, 78, 90, 901], rotated around pivot k=5  becomes [47, 
    78, 90, 901, 10, 30, 40, 42, 42]. 
Return TRUE if t exists in the rotated, sorted array arr, and FALSE otherwise, while minimizing the number of operations in the 
search.

Constraints  
1 ≤ arr.length ≤ 1000 
-10^4 ≤ arr[i] ≤ 10^4   
arr is guaranteed to be rotated at some pivot index. 
-10^4 ≤ t ≤ 10^4  
"""

def search(arr, t):

    # Initializing left and right pointer for modified binary search.
    left, right = 0, len(arr)-1

    while left<=right:
        mid = (left+right)//2
        if arr[mid]==t:
            return True
        
        # If this is true it means that the left side is sorted
        if arr[left]<arr[mid]:
            if arr[left]<=t<arr[mid]:
                right = mid-1
            else:
                left = mid+1
        # If this is true it means that the right side is sorted
        elif arr[mid]<arr[right]:
            if arr[mid]<t<=arr[right]:
                left =  mid +1
            else:
                right = mid-1
        # If above cases fail, elements at left, right and mid are equal.
        # We check the value at right equals target otherwise decrement the value of right
        elif arr[right]==t:
            return True
        else:
            right -= 1
    return False