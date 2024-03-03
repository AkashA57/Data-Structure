"""
Given the head of a linked list, the nodes in it are assigned to each group in a sequential manner. The length of these groups 
follows the sequence of natural numbers. Natural numbers are positive whole numbers denoted by (1,2,3,4...).
In other words: 
            The 1st node is assigned to the first group. 
            The 2nd and 3rd nodes are assigned to the second group. 
            The 4th, 5th , and 6th nodes are assigned to the third group, and so on.

Your task is to reverse the nodes in each group with an even number of nodes and return the head of the modified linked list.
Note: The length of the last group may be less than or equal to 1 + the length of the second to the last group.

Constraints: 1 ≤ Number of nodes ≤ 500 
             0 ≤ LinkedListNode.data ≤ 10^3
"""

# Time complexity: O(n), Space complexity: O(1)
def reverse_even_length_groups(head):
  # 'prev' node points to the end of the previous group. 'curr' points to the current node.
  prev, curr= head, head
  # 'count' keeps count of the number of nodes traversed in the current group
  count = 0 
  # Initializing the group as 2 since we don't need to swap the group containing odd length.
  # Hence, skipping 1.
  group = 2
  while curr:
    curr = curr.next
    if curr:
      count += 1
    if count == group or (curr is None and count<=group):
      if count >0 and count%2==0:
        curr = reverse(prev, count)
      # When we reach end of the group, we readjust prev, count and group.
      count = 0
      group += 1
      prev = curr
  return head

# Reversing the nodes while reordering the pointer for previous and next group.
def reverse(prev_group, count):
  prev = None
  curr = prev_group.next
  for i in range(count):
    curr.next, curr, prev = prev, curr.next, curr
  end = prev_group.next
  prev_group.next = prev
  end.next = curr 
  
  return end

"""
Alternate solution
"""
# def reverse_even_length_groups(head):
#     prev = head  
#     l = 2

#     while prev.next:
#         node = prev
#         n = 0
#         for i in range(l):
#             if not node.next:
#                 break
#             n += 1
#             node = node.next
#         if n % 2:  
#             prev = node
#         else:      
#             reverse = node.next
#             curr = prev.next
#             for j in range(n):
#                 curr_next = curr.next
#                 curr.next = reverse
#                 reverse = curr
#                 curr = curr_next
#             prev_next = prev.next
#             prev.next = node
#             prev = prev_next
#         l += 1

#     return head




