# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        slowptr = head
        fastptr = head

        while fastptr.next and fastptr.next.next:
            slowptr = slowptr.next
            fastptr = fastptr.next.next

            if slowptr == fastptr:
                return True
        return False
