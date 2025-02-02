# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        head_new = ListNode(0)
        first_end = head_new
        second_start = ListNode(0)
        second_end = second_start

        while head:
            if head.val < x:
                first_end.next = head
                first_end = first_end.next
            else:
                second_end.next = head
                second_end = second_end.next

            head = head.next

        second_end.next = None
        first_end.next = second_start.next

        return head_new.next

