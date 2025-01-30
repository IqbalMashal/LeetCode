# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return 
        temp = head
        counter = 0
        while(temp is not None):
            counter+= 1
            temp = temp.next
        temp = head
        for _ in range(counter//2):
            temp  = temp.next
        head = temp 
        return head