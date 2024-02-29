"""
Given the linked list and an integer, k, return the head of the linked list after swapping the values of the k th node from the 
beginning and the k th node from the end of the linked list.
Note: We'll number the nodes of the linked list starting from 1 to n.
Constraints: 
            The linked list will have n number of nodes. 
            1 ≤ k ≤ n ≤ 500 
            -5000 ≤ Node.value ≤ 5000
"""

def swap_nodes(head, k):

    front = head
    # Pointing front to the kth item from beginning
    for i in range(k-1):
        front  = front.next

    end = head
    traverse = front
    # Pointing end to the kth item from end
    while traverse.next:
        end = end.next
        traverse = traverse.next

    # Swapping data
    front.data, end.data = end.data, front.data
    
    return head