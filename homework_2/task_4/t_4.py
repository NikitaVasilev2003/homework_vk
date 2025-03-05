"""Необходимо написать функцию, которая принимает на вход
односвязный список и некоторое целое число val.
Необходимо удалить узел из списка, значение которого равно val.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeElements(head: ListNode, val: int) -> ListNode:
    dummy = ListNode(next=head)
    prev = dummy
    cur = head
    while cur:
        if cur.val == val:
            prev.next = cur.next
        else:
            prev = cur
        cur = cur.next
    return dummy.next
