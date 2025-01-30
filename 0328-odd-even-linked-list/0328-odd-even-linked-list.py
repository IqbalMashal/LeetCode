# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None  # ❌ Previously returned nothing, should return None

        odd = head
        even = head.next
        evenHead = even

        while even and even.next:  # ✅ Prevent infinite loop
            odd.next = even.next  # Move odd forward
            odd = odd.next
            even.next = odd.next  # Move even forward
            even = even.next

        odd.next = evenHead  # Connect odd list to even list

        return head  # ✅ Return head, not odd