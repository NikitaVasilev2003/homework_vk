"""Написать функцию, которая принимает на вход два отсортированных
односвязных списка и объединяет их в один отсортированный список.
При этом затраты по памяти должны быть O(1)"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_sorted_lists(list1: ListNode, list2: ListNode) -> ListNode:
    merge_list = ListNode(None)
    prev = merge_list
    while list1 and list2:
        if list1.val < list2.val:
            prev.next = list1
            list1 = list1.next
        else:
            prev.next = list2
            list2 = list2.next
        prev = prev.next
    if list1:
        prev.next = list1
    if list2:
        prev.next = list2
    return merge_list.next
