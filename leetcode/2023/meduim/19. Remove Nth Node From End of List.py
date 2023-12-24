# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return

        nodes_link = {}
        counter = 1

        while head:
            nodes_link[counter] = head
            head = head.next
            counter += 1

        size = counter - 1

        if n > size:
            return None

        next_before_remove = nodes_link.get(size - n)
        next_after_remove = nodes_link.get(size - n + 2)

        if next_before_remove:
            next_before_remove.next = next_after_remove
        else:
            return next_after_remove

        return nodes_link.get(1)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class SolutionRecursive:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        length = self.recurcive(head, n, None)

        if n > length:
            return None

        if n == length:
            return head.next

        return head

    def recurcive(self, head, n, prev_head):
        if not head:
            return 0

        count = self.recurcive(head.next, n, head) + 1

        if count == n and prev_head is not None:
            prev_head.next = head.next

        return count
