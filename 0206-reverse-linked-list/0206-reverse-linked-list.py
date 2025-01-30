# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None  # Return None if the list is empty
        
        previous = None
        current = head
        
        while current is not None:
            next_node = current.next  # Save the next node
            current.next = previous    # Reverse the link
            previous = current         # Move previous to current
            current = next_node        # Move to the next node
        
        return previous  #