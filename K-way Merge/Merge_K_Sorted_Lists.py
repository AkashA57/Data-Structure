"""
Given an array of k sorted linked lists, your task is to merge them into a single sorted linked list and return the head of this 
linked list.
Constraints:
k = lists.length 
0 ≤ k ≤ 10^3 
0 ≤ lists[i].length ≤ 500 
-10^3 ≤ lists[i][j] ≤ 10^3 
Each lists[i] is sorted in ascending order. 
The sum of all lists[i].length will not exceed 10^3.
"""

from linked_list import LinkedList
from linked_list_node import LinkedListNode

from linked_list import LinkedList
from linked_list_node import LinkedListNode

def merge_k_lists(lists):
    if len(lists)>0:
        step = 1
        while step < len(lists): 
            for i in range(0, len(lists)-step, step * 2):
                lists[i].head = merge_two_list(lists[i].head, lists[i+step].head)
            step *= 2
        return lists[0].head
        
    return None

def merge_two_list(head1, head2):
    dummy = LinkedListNode(-1)
    head = dummy
    while head1 and head2:
        if head1.data<=head2.data:
            dummy.next = head1
            dummy = head1
            head1 = head1.next
        else:
            dummy.next = head2
            dummy = head2
            head2 = head2.next
    if head2:
        dummy.next = head2
    if head1:
        dummy.next = head1
    
    return head.next

        

merge_k_lists([LinkedList.create_linked_list([2]),LinkedList.create_linked_list([1,2,4]),LinkedList.create_linked_list([25,56,66,72])])

        
