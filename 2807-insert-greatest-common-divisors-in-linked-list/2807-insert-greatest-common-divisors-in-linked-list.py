# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or head.next == None:
            return head

        temp = head

        while temp.next is not None:
            num1 = temp.val
            num2 = temp.next.val
            gcd = math.gcd(num1, num2)

            new_node = ListNode(gcd)
            new_node.next = temp.next
            temp.next = new_node
            temp = temp.next.next


        return head

        
        