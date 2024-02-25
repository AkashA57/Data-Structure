"""
Given the head of a singly linked list, reverse the linked list and return its updated head. 
Constraints: Let n be the number of nodes in a linked list. 
1≤ n ≤ 500  
-5000 ≤ Node.value ≤ 5000
"""

 #Time complexity: O(n). Space complexity:O(1)
def reverse(head):

    before = None
    after= None
    current = head

    while current:
        after = current.next
        current.next = before
        before = current
        current = after
    return before
