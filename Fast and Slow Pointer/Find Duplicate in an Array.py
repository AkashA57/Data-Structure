""" Given an unsorted array of positive numbers, nums, such that the values lie in the range [1,n] , 
inclusive, and that there are n+1 numbers in the array, find and return the duplicate number present in nums. 
There is only one repeated number in nums.

Constraints: 
1≤n≤10^3 
nums.length=n+1 
1 ≤ nums[i] ≤ n
All the integers in nums are unique, except for one integer that will appear more than once. """

def find_duplicate(nums):

    # Replace this placeholder return statement with your code
    len_nums = len(nums)
    for i in range(len_nums):
        slow_pointer = (i+1)%len_nums
        fast_pointer = (i+2)%len_nums
        
        while slow_pointer!=fast_pointer:
            if nums[slow_pointer]==nums[fast_pointer]:
                return nums[slow_pointer]
            slow_pointer = (slow_pointer+1)%len_nums
            fast_pointer = (slow_pointer+2)%len_nums
    
    return 0

print(find_duplicate([1,3,6,2,7,3,5,4]))