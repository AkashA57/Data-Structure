"""
We are given an input array, tasks, which contains the start and end times of n tasks. Your task is to find the minimum number of
machines required to complete these n tasks. 
Constraints: 
n == tasks.length 
1 <= tasks.length <= 10^3 
0 ≤ tasksi.start < tasksi.end ≤ 10^6
"""

import heapq

def tasks(tasks_list):

    # Converting list to heap for easy access of interval having the earliest start time
    heapq.heapify(tasks_list)
    # Intitializing heap to store interval having the earliest end time
    end_of_interval = []

    # Popping first element from tasks_list and storing the end time to the end_of_interval
    end = heapq.heappop(tasks_list)[1]
    heapq.heappush(end_of_interval, end)

    # Lopping through rest of the tasks and comparing whether the start time of the tasks is later than the ealiest end time.
    # If yes, we have a machine available. If not, we need a new machine.
    while tasks_list:
        if tasks_list[0][0]>=end_of_interval[0]:
            heapq.heappop(end_of_interval)
        end = heapq.heappop(tasks_list)[1]
        heapq.heappush(end_of_interval, end)
    
    return len(end_of_interval)