"""
We’re given a character array, tasks, where each character represents a unique task. These tasks need to be performed by a single
CPU, with each task taking one unit of time. The tasks can be performed in any order. At any given time, a CPU can either perform 
some task or stay idle. 
For the given tasks, we are also provided with a positive integer value, n, which represents the cooling period between any two 
identical tasks. This means that the CPU must wait for at least n units of time before it performs the same task again. For example, 
if we have the tasks [A,B,A,C] and n = 2, then after performing the first A task, the CPU will wait for at least 2 units of time to 
perform the second A task. During these 2 units of time, the CPU can either perform some other task or stay idle. Given the two 
input values, tasks and n, find the least number of units of time the CPU will take to perform the given tasks.
Constraints
1 ≤ tasks.length ≤ 1000 
tasks consists of uppercase English letters. 
0 ≤ n ≤ 100 
"""

from collections import Counter

#Time complexity O(N). Sorting is O(1) since there are 26 items. Space Complexity O(1)
def least_time(tasks, n):
    #Counts frequency of task(Counter is a child class of dictionary)
    frequencies = Counter(tasks)

    #Sorting according to the frequency
    frequencies = dict(sorted(frequencies.items(), key=lambda x:x[1]))
    max_freq = frequencies.popitem()[1]

    #Suppose max frequency in tasks is {'A':3,.....} and n = 2. Then, max possible idle_time is A _ _ A _ _ A denoted by the equation below.
    idle_time = (max_freq - 1) * n

    #Updating idle time as we iterate through other tasks
    while frequencies and idle_time > 0:
        #If there are multiple tasks with max freq, we cannot simply decrease current value. Instead we decrease max-1 from idle_time.
        idle_time -= min(max_freq - 1, frequencies.popitem()[1]) 
    idle_time = max(0, idle_time)

    return len(tasks) + idle_time

print(least_time(["A", "A", "B", "B"] , 2))