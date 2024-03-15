"""
Given an integer array, nums, and an integer, k, there is a sliding window of size k, which is moving from the very left to the very
right of the array. We can only see the k numbers in the window. Each time the sliding window moves right by one position. Given 
this scenario, return the median of the each window. Answers within 10^-5 of the actual value will be accepted.
Constraints:
            1 ≤ k ≤ nums.length ≤ 10^3
            -2^31 ≤ nums[i] ≤ 2^31-1
"""

from heapq import *
def median_sliding_window(nums, k):

    # Creating max heap and min heap to efficiently calculate median.
    small_num_maxh = []
    large_num_minh = []
    median = []
    balance = 0
    old_val = {}

    #Storing k values in max heap
    for i in range(k):
        heappush(small_num_maxh, -nums[i])

    #Removing k//2 large value from max heap and storing it in min heap.
    for i in range(k//2):
        max_num = -heappop(small_num_maxh)
        heappush(large_num_minh, max_num)

    for i in range(k-1, len(nums)):

        # Calculating median for the k window depending on whether it is even or odd
        if k%2==0:
            mean = (large_num_minh[0]-small_num_maxh[0])/2
            median.append(mean)
        else:
            median.append(-small_num_maxh[0]) 
        
        #Terminating the loop once there is no more incoming number.
        if i+2>len(nums):
            break
        outgoing_num = nums[i-k+1]
        incoming_num = nums[i+1]

        # Keeping track of whether the initial balance is maintained in the heap.
        if outgoing_num<=-small_num_maxh[0]:
            balance -= 1
        else:
            balance += 1

        if incoming_num<=-small_num_maxh[0]:
            balance += 1
            heappush(small_num_maxh, -incoming_num)
        else:
            balance -= 1
            heappush(large_num_minh, incoming_num)

        # Keeping track of the old values that are still in the heap.
        old_val[outgoing_num] = old_val.get(outgoing_num, 0) + 1

        # If balance is 0, then it means the outgoing num and incoming num lies in the same half(min or max) of the heap.
        # Else we need to rebalance accordingly.
        if balance<0:
            heappush(small_num_maxh, -heappop(large_num_minh))
        elif balance>0:
            heappush(large_num_minh, -heappop(small_num_maxh)) 

        # If old values is in the 0th index of the heaps we can simply pop it since it is no longer needed to calculate the median.
        while small_num_maxh and old_val.get(-small_num_maxh[0], 0)>0:
            old_val[-small_num_maxh[0]] -= 1 
            heappop(small_num_maxh)

        while large_num_minh and old_val.get(large_num_minh[0], 0)>0:
            old_val[large_num_minh[0]] -= 1 
            heappop(large_num_minh)

        balance = 0

    return median

print(median_sliding_window([1,3,-1,-3,5,3,6,7] , 3), "Expected: [1,-1,-1,3,5,6]")

"""
Course Solution
"""

# def median_sliding_window(nums, k):
#     medians = []

#     outgoing_num = {}

#     small_list = []

#     large_list = []

#     for i in range(0, k):
#         heappush(small_list, -1 * nums[i])

#     for i in range(0, k//2):
#         element = heappop(small_list)
#         heappush(large_list, -1 * element)

#     balance = 0

#     i = k
#     while True:
#         if (k & 1) == 1:
#             medians.append(float(small_list[0] * -1))
#         else:
#             medians.append((float(small_list[0] * -1) + float(large_list[0])) * 0.5)

#         if i >= len(nums):
#             break

#         out_num = nums[i - k]

#         in_num = nums[i]
#         i += 1

#         if out_num <= (small_list[0] * -1):
#             balance -= 1
#         else:
#             balance += 1

#         if out_num in outgoing_num:
#             outgoing_num[out_num] = outgoing_num[out_num] + 1
#         else:
#             outgoing_num[out_num] = 1

#         if small_list and in_num <= (small_list[0] * -1):
#             balance += 1
#             heappush(small_list, in_num * -1)
#         else:
#             balance -= 1
#             heappush(large_list, in_num)

#         if balance < 0:
#             heappush(small_list, (-1 * large_list[0]))
#             heappop(large_list)
#         elif balance > 0:
#             heappush(large_list, (-1 * small_list[0]))
#             heappop(small_list)

#         balance = 0

#         while (small_list[0] * -1) in outgoing_num and (outgoing_num[(small_list[0] * -1)] > 0):
#             outgoing_num[small_list[0] * -1] = outgoing_num[small_list[0] * -1] - 1
#             heappop(small_list)

#         while large_list and large_list[0] in outgoing_num and (outgoing_num[large_list[0]] > 0):
#             outgoing_num[large_list[0]] = outgoing_num[large_list[0]] - 1
#             heappop(large_list)

#     return medians