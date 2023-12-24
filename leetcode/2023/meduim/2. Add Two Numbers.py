# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        # [1,0,0,1] [2]
        # [1,0,0,1] []
        if not l1 and not l2:
            return None

        if not l1:
            return l2

        if not l2:
            return l1

        add = 0
        prev = None
        head = None

        while l1 or l2:
            if not l1:
                l1 = ListNode(0, None)

            if not l2:
                l2 = ListNode(0, None)

            value = l1.val + l2.val + add

            if value >= 10:
                value = value % 10
                add = 1
            else:
                add = 0

            current = ListNode(value, None)

            if not head:
                head = current
            else:
                prev.next = current

            prev = current

            l1 = l1.next
            l2 = l2.next

        if add == 1:
            current.next = ListNode(1, None)

        return head


# (8 add =1) (9 add=1) (9 add=1) (9 add = 1) (0 add =1) ()
