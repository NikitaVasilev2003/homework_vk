class Node:
    """Класс для узла связанного списка."""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    """Класс для связанного списка."""

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        """Добавляет узел в конец списка."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def __str__(self):
        """Возвращает строковое представление списка."""
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        return " -> ".join(nodes) + " -> None"


def array_to_linked_list(arr):
    """Преобразует массив в связанный список."""
    linked_list = LinkedList()
    for item in arr:
        linked_list.append(item)
    return linked_list
