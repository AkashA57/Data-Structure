from min_heap import *
from max_heap import *

# Tip: You may use some of the code templates provided
# in the support files

class MedianOfStream:
  def __init__(self):
    # Write your code here
    self.maxheap = max_heap()
    self.minheap = min_heap()
    self.len_max = 0
    self.len_min = 0

  # This function should take a number and store it
  def insert_num(self, num):
    # Here we are figuring out whether to add the num to the maxheap(for small half) or minheap(for large half)
    if self.len_min>0 and num>self.minheap.get_min():
      temp = heappop(self.minheap.min_heap_list)
      self.minheap.insert(num)
      num = temp

    self.maxheap.insert(num)
    self.len_max += 1
    # As soon as the length of the maxheap is greater by 2 than the minheap, we balance out the heaps.
    if self.len_max==self.len_min+2:
      self.minheap.insert(-heappop(self.maxheap.max_heap_list))
      self.len_min += 1
      self.len_max -= 1
    
  # This function should return the median of the stored numbers
  def find_median(self):
    # When both heaps are of same lenght, total length is even. Calculating average if there is even numbers. 
    if self.len_max==self.len_min:
      return ((self.maxheap.get_max()+self.minheap.get_min())/2)
    # When odd
    return self.maxheap.get_max()
  

"""
Alternate solution
"""
#   class MedianOfStream:
    
#     def __init__(self):
#         self.max_heap_for_smallnum = []
#         self.min_heap_for_largenum = []

#     def insert_num(self, num):
#         if not self.max_heap_for_smallnum or -self.max_heap_for_smallnum[0] >= num:
#             heappush(self.max_heap_for_smallnum, -num)
#         else:
#             heappush(self.min_heap_for_largenum, num)

#         if len(self.max_heap_for_smallnum) > len(self.min_heap_for_largenum) + 1:
#             heappush(self.min_heap_for_largenum, -heappop(self.max_heap_for_smallnum))
#         elif len(self.max_heap_for_smallnum) < len(self.min_heap_for_largenum):
#             heappush(self.max_heap_for_smallnum, -heappop(self.min_heap_for_largenum))

#     def find_median(self):
#         if len(self.max_heap_for_smallnum) == len(self.min_heap_for_largenum):

#             return -self.max_heap_for_smallnum[0] / 2.0 + self.min_heap_for_largenum[0] / 2.0

#         return -self.max_heap_for_smallnum[0] / 1.0
