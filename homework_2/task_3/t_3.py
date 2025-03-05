"""Дан связный список. Необходимо найти середину списка.
Сделать это необходимо за O(n) без дополнительных аллокаций
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middleNode(head: ListNode) -> ListNode:
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow
