# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # 1 2 3 -> 1 2 3
        # 1 1 1 1 -> 1
        # 3 -> 3

        # prev_element = None

        # head_input = head

        # while head is not None:
        #     if prev_element is None:
        #         prev_element = head

        #     elif prev_element.val == head.val:
        #         prev_element.next = head.next
        #     else:
        #         prev_element = head

        #     head = head.next

        # return head_input

        if head is None:
            return head

        prev_element = head
        pointer = head

        head = head.next

        while head:
            if head.val != prev_element.val:
                prev_element.next = head
                prev_element = head

            head = head.next

        prev_element.next = None

        return pointer


# beautiful


def deleteDuplicates(self, head):
    curr = head
    while curr and curr.next:
        if curr.next.val == curr.val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head
