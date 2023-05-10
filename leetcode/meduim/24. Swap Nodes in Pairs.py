# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1 2 3 4 5 6
        # 2 1 4 3 6 5

        if not head or not head.next:
            return head

        first = head
        second = head.next
        head = second.next

        new_head = second
        new_head.next = first

        prev = first

        while head:
            first = head
            second = head.next

            if not second:
                prev.next = first
                first.next = None
                break

            head = second.next


            prev.next = second
            second.next = first
            prev = first
            first.next = None



        return new_head




