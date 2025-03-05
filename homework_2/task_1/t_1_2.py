"""Дан односвязный список. Необходимо проверить, является ли этот список циклическим.
2 способ с доп памятью
"""


class ListNode:
    def __init__(self, x) -> None:
        self.val = x
        self.next = None


def hasCycle_2(head: ListNode) -> bool:
    cycle_set = set()
    while head:
        if head in cycle_set:
            return True
        cycle_set.add(head)
        head = head.next
    return False
