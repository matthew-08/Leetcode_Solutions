# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        curr1 = l1
        curr2 = l2
        carryNum = 0

        while curr1 or curr2 or carryNum:
            c1 = curr1.val if curr1 else 0
            c2 = curr2.val if curr2 else 0

            add = c1 + c2 + carryNum
            carryNum = add // 10
            add = add % 10
            curr.next = ListNode(add)

            curr = curr.next
            
            curr1 = curr1.next if curr1 else None
            curr2 = curr2.next if curr2 else None
        return dummy.next