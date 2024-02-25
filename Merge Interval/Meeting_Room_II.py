"""
We are given an input array of meeting time intervals, intervals, where each interval has a start time and an end time. Your task 
is to find the minimum number of meeting rooms required to hold these meetings.
An important thing to note here is that the specified end time for each meeting is exclusive.
Constraints:
1 <= intervals.length <= 10^3
0 ≤ start(i) < end (i) ≤ 10^6
"""

import heapq

def find_sets(intervals):

    # Sorting the intervals in ascending order. Time complexity O(nlogn).
    intervals = sorted(intervals)

    # Initialize heap with end time of the first interval.
    heap = [intervals[0][1]]

    # Compares current start time with end time of root of the heap. 
    # If current start time is greater than heap root. Replace root with current end time, else add another room.
    for i in range(1, len(intervals)):
        if intervals[i][0]>=heap[0]:
            heapq.heapreplace(heap, intervals[i][1])
        else:
            heapq.heappush(heap, intervals[i][1])

    return len(heap)

print(find_sets([[2,8],[3,4],[3,9],[5,11],[8,20],[11,15]]))