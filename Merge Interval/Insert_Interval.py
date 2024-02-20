"""
Given a sorted list of nonoverlapping intervals and a new interval, your task is to insert the new interval into the correct 
position while ensuring that the resulting list of intervals remains sorted and nonoverlapping. Each interval is a pair of 
nonnegative numbers, the first being the start time and the second being the end time of the interval. 

Constraints: 
0 ≤ existing_intervals.length ≤ 10^4  
existing_intervals[i].length, new_interval.length == 2 
0≤ start time ≤end time ≤10^4 
The list of intervals is sorted in ascending order based on the start time .
"""
def insert_interval(existing_intervals, new_interval):

  # Replace this placeholder return statement with your code
  n = len(existing_intervals)
  i = 0
  output= []
  while i<n and existing_intervals[i][0]<new_interval[0]:
    output.append(existing_intervals[i])
    i += 1

  if not output or output[-1][1]<new_interval[0]:
    output.append(new_interval)
  else:
    output[-1][1] = max(output[-1][1], new_interval[1])

  for i in range(i, n):
    if output[-1][1]<existing_intervals[i][0]:
      output.append(existing_intervals[i])
    else:
      output[-1][1] = max(output[-1][1], existing_intervals[i][1])

  return output