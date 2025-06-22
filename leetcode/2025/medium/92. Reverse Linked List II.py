# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        new_head = ListNode(val=0, next=head)
        head = new_head
        first = new_head
        stack = []

        while head and head.val <= right:
            if head.val < left:
                first = head
            else:
                stack.append(head)

            head = head.next

        for i in reversed(stack):
            first.next = i
            first = first.next

        first.next = head

        return new_head.next








