"""
Given a singly linked list with � n nodes and two positions, left and right, the objective is to reverse the nodes of the list from 
left to right. Return the modified list.
1 ≤n ≤ 500
-5000 ≤ node.data ≤ 5000
1 ≤ left ≤ right ≤ n
"""

from linked_list_node import LinkedListNode


def reverse_between(head, left, right):

  # Replace this placeholder return statement with your code
  dummy = LinkedListNode(0, head)
  previous = dummy

  # Pointing previous to the node just before the left node
  for i in range(left-1):
    previous = previous.next
  
  current = previous.next
  start = None

  # Reversing the nodes starting from left until right
  for i in range(left, right+1):
    nxt = current.next
    current.next = start
    start = current
    current = nxt
  
  #Rearranging the start and end pointers of the reversed nodes.
  previous.next.next = current
  previous.next = start 
  return dummy.next