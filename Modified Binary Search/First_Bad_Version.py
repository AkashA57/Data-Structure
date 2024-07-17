"""
The latest version of a software product fails the quality check. Since each version is developed upon the previous one, all the 
versions created after a bad version are also considered bad.  
Suppose you have n versions with the IDs [1,2,...,n], and you have access to an API function that returns TRUE if the argument is 
the ID of a bad version.  
Find the first bad version that is causing all the later ones to be bad. Additionally, the solution should also return the number 
of API calls made during the process and should minimize the number of API calls too.

Constraints:  
1 ≤ first bad version ≤ n ≤ 10^5  
"""

# -- DO NOT CHANGE THIS SECTION -----------------
    
import main as api_call

def is_bad_version(v): # is_bad_version() is the API function that returns true or false depending upon whether the provided version ID is bad or not
    return api_call.is_bad(v)
# ----------------------------------------------- 

def first_bad_version(n):

    # Initializing counter to keep track of no of calls. 
    counter = 0
    left, right = 1, n
    # Running the loop until left pointer crosses the right
    while left<=right:
        # Mid as a mean of left and right indices. 
        mid = (left+right)//2
        # If mid is a bad version we ignore second half of the array
        if is_bad_version(mid):
            right = mid-1
        # If mid is a good version we ignore first half of the array
        else:
            left = mid+1
        counter += 1
    return [left, counter]

