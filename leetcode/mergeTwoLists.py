# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        current = head = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1, current = list1.next, list1
            else:
                current.next = list2
                list2, current = list2.next, list2

        if list1 or list2:
            current.next = list1 or list2

        return head.next






# не заработало (лимит по времени)

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        counter_ = {key:0 for key in range(-100, 101)}

        while list1 is not None and list2 is not None:
            if list1.next is not None:
                l = list1
                list1 = list1.next
            elif list2.next is not None:
                l = list2
                list2 = list2.next
            count = counter_.get(l.val)
            counter_[l.val] = count or 1


        prev = None
        head = None
        for key, value in reversed(counter_.items()):
            if value > 0:
                for num in range(value):
                    head = ListNode(val=key, next=prev)
                    prev=head


        return head











