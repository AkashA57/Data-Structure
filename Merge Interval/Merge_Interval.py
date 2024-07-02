"""
We are given an array of closed intervals, intervals, where each interval has a start time and an end time. 
The input array is sorted with respect to the start times of each interval. 
For example, intervals = [ [ 1 , 4 ] , [ 3 , 6 ] , [ 7 , 9 ] ] [ [1,4], [3,6], [7,9] ] is sorted in terms of start times 1 , 3 1, 3 , and 7 7 . 
Your task is to merge the overlapping intervals and return a new output array consisting of only the non-overlapping intervals. 
Constraints: 
1≤ intervals.length ≤ 10^4  
intervals[i].length = 2 
0 ≤ start time ≤ end time ≤ 10^4
"""

def merge_intervals(intervals):

    # Replace this placeholder return statement with your code
    result = [intervals[0]]
    for index in range(1,len(intervals)):
        if result[-1][1]>=intervals[index][0]:
            result[-1][1] = max(result[-1][1], intervals[index][1])
        else:
            result.append(intervals[index])

    return result

