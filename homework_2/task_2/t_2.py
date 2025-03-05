"""Необходимо написать функцию, которая принимает на вход односвязный
список и разворачивает его.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: ListNode) -> ListNode:
    if not head:
        return head
    cur = head
    prev = None
    while cur:
        tmp = cur.next
        cur.next = prev
        prev = cur
        cur = tmp
    return prev
