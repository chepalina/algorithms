# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(val=None, next=head)
        curr = dummy
        duplicate_val = None

        while curr.next is not None and curr.next.next is not None:
            if curr.next.val != curr.next.next.val:
                curr = curr.next
            else:
                temp = curr.next.next.next
                while curr.next.val == temp.val:
                    temp = temp.next

                curr.next = temp

        return dummy.next
