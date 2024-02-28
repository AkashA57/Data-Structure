"""
Given the head of a singly linked list, reorder the list as if it were folded on itself. For example, if the list is represented as 
follows:
            L 0 ​→  L 1  → L 2  → … → L n-2  →  L n-1  → L n 
This is how you’ll reorder it:
            L 0 ​→  L n  ​→  L 1 →  L n-1 → L 2  → L n-2 →.....
You don’t need to modify the values in the list's nodes; only the links between nodes need to be changed. 
Constraints: 
The range of number of nodes in the list is [1,500]. 
- 5000 ≤ Node.value ≤ 5000 
"""
            
# from linked_list import LinkedList
# from linked_list_node import LinkedListNode
            
# def reorder_list(head):

#     # Finding middle of the linked list
#     slow_pointer, fast_pointer = head, head
#     while fast_pointer and fast_pointer.next:
#         slow_pointer = slow_pointer.next
#         fast_pointer = fast_pointer.next.next

#     # Reversing second half of the LinkedList
#     prev = None
#     curr = slow_pointer
#     while curr:
#         nxt = curr.next
#         curr.next = prev
#         prev = curr
#         curr = nxt

#     first_part = head
#     second_part = prev
#     while second_part.next:
#         temp1 = first_part.next
#         temp2 = second_part.next
#         first_part.next = second_part
#         first_part = temp1
#         second_part.next = first_part
#         second_part = temp2
#     return head

def reorder_list(head):
    if not head:
        return head
    
    # find the middle of linked list
    # in 1->2->3->4->5->6 find 4 
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next 
        
    # reverse the second part of the list
    # convert 1->2->3->4->5->6 into 1->2->3 and 6->5->4
    # reverse the second half in-place
    prev, curr = None, slow
    while curr:
        curr.next, prev, curr = prev, curr, curr.next       

    # merge two sorted linked lists
    # merge 1->2->3 and 6->5->4 into 1->6->2->5->3->4
    first, second = head, prev
    while second.next:
        first.next, first = second, first.next
        second.next, second = first, second.next
    
    return head

