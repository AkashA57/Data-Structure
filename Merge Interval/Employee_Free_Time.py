"""
You’re given a list containing the schedules of multiple employees. Each person’s schedule is a list of non-overlapping intervals 
in sorted order. An interval is specified with the start and end time, both being positive integers. Your task is to find the list 
of finite intervals representing the free time for all the employees. 
Constraints: 
1≤ schedule.length , schedule[i].length ≤ 50
0≤ interval.start < interval.end ≤ 10^8, where interval is any interval in the list of schedules.
"""

import heapq

def employee_free_time(schedule):  
          
    
    len_schedule = len(schedule)
    min_interval = []
    result = []
    #Adding first interval from each employee's schedule
    for i in range(len_schedule):
        min_interval.append((schedule[i][0][0], i, 1))
    #Storing the interval as min Heap
    heapq.heapify(min_interval)

    #Setting previous time as an end time of the earliest interval
    start, emp_ind, emp_sch_ind = min_interval[0]
    previous = schedule[emp_ind][emp_sch_ind-1][1]

    #Pop the smallest interval and compare it with the previous interval.
    #If current interval start >previous interval, add it to the result list.
    #Set previous interval as max(current interval end, previous interval)
    while min_interval:
        start, emp_ind, emp_sch_ind = heapq.heappop(min_interval)
        end = schedule[emp_ind][emp_sch_ind-1][1]

        if emp_sch_ind<len(schedule[emp_ind]):
            heapq.heappush(min_interval, (schedule[emp_ind][emp_sch_ind][0], emp_ind, emp_sch_ind+1))
        if start>previous:
            result.append([previous, start])
        previous = max(previous, end)
    return result

print(employee_free_time([[[3, 5], [8, 10]], [[4, 6], [9, 12]], [[5, 6], [8, 10]]]))
    