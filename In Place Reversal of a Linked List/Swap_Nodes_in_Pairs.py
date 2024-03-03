"""
Given a singly linked list, swap every two adjacent nodes of the linked list. After the swap, return the head of the linked list.

Note: Solve the problem without modifying the values in the list’s nodes. In other words, only the nodes themselves can be changed.

Constraints: The number of nodes in the list is in the range [0,100]. 
             0 ≤ Node.value ≤ 100 
"""

def swap_pairs(head):

    curr = head
    # Creating dummy node for the access of head.
    dummy = LinkedListNode(0, head)
    prev_end = dummy
    
    # Making sure that there are pair of nodes.
    while curr and curr.next:
        prev = prev_end
        # Swapping pair of nodes.
        for i in range(2):
            curr.next, curr, prev = prev, curr.next, curr
        # Reconnecting the swapped nodes with rest of the linked list.
        prev_end.next, prev.next.next = prev, curr
        # Updating previous end of pair of nodes with current endafter swapping.
        prev_end = prev.next
        
    return dummy.next