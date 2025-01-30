# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head is None:
            return None
            
        greater_dummy = ListNode(0)
        less_dummy = ListNode(0)
        
        less = less_dummy
        greater = greater_dummy
        
        current = head
        
        while current:
            if current.val < x:
                less.next = current
                less = less.next
            else:
                greater.next = current
                greater = greater.next
            current = current.next
        
        greater.next = None
        less.next = greater_dummy.next
        
        head = less_dummy.next
        tail = greater
        
        return head