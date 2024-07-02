"""
The task is to reverse the nodes in groups of k in a given linked list, where k is a positive integer, and at most the length of 
the linked list. If any remaining nodes are not part of a group of k, they should remain in their original order. 
It is not allowed to change the values of the nodes in the linked list. Only the order of the nodes can be modified.

Note: Use only O(1) extra memory space.
"""
from linked_list import LinkedList
from linked_list_node import LinkedListNode
from linked_list_reversal import reverse_linked_list

#My solution
# def reverse_k_groups(head, k):
  
#     # Replace this placeholder return statement with your code
#     length = 0
#     traverse = head
#     result = None
#     while traverse:
#         length += 1
#         if length==k:
#             result = traverse
#         traverse = traverse.next

#     groups = length//k

#     prev_gr_end = None
#     curr = head
#     for i in range(groups):
#         prev = None
#         curr_gr_end = curr
#         for j in range(k):
#             nxt = curr.next
#             curr.next = prev
#             prev = curr
#             curr = nxt
#         if prev_gr_end:
#             prev_gr_end.next = prev
#         prev_gr_end = curr_gr_end
#         curr_gr_end.next = curr

#     return result

# linkList = LinkedList()
# linkList.create_linked_list([3, 4, 5, 6, 2, 8, 7, 7])
  
# linkList.head = reverse_k_groups(linkList.head, 3)

# print(linkList.__str__())


def reverse_k_groups(head, k):

    dummy = LinkedListNode(0)
    dummy.next = head
    ptr = dummy
 
    # Looping until the end of list
    while(ptr != None):

        tracker = ptr
        #Checking if k number of nodes exist. If not, break out of the loop
        for i in range(k):

            if tracker == None:
                break
       
            tracker = tracker.next

        if tracker == None:
            break
            
        #Reversing k nodes, where previous = head of the reversed list and current = head of the remaining nodes.
        previous, current = reverse_linked_list(ptr.next, k)

        last_node_of_reversed_group = ptr.next
        last_node_of_reversed_group.next = current
        ptr.next = previous
        ptr = last_node_of_reversed_group

    return dummy.next
