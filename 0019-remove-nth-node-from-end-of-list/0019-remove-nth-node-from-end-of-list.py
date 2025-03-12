# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        
        # First, calculate the length of the linked list
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
        
        # If we need to remove the head
        if length == n:
            return head.next
        
        # Find the node just before the one we want to remove
        ever = head
        for i in range(length - n - 1):
            ever = ever.next
        
        # Remove the N-th node from the end
        ever.next = ever.next.next
        
        return head