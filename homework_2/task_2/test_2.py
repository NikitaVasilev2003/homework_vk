import sys

sys.path.append("/Users/nikitavasilev/Desktop/вк_задачи_по_алгортмам")
from t_2 import ListNode, reverseList
from homework_2.node_1 import LinkedList
import unittest


class CustomTestResult(unittest.TextTestResult):
    def startTest(self, test: unittest.TestCase) -> None:
        super().startTest(test)
        print(f"🚀 Запуск теста: {test._testMethodName} {test._testMethodDoc}")

    def addSuccess(self, test: unittest.TestCase) -> None:
        super().addSuccess(test)
        print(f"✅ Тест пройден: {test._testMethodName}")

    def addFailure(self, test: unittest.TestCase, err) -> None:
        super().addFailure(test, err)
        print(f"❌ Тест не пройден: {test._testMethodName}")

    def addError(self, test: unittest.TestCase, err) -> None:
        super().addError(test, err)
        print(f"⚠️ Ошибка в тесте: {test._testMethodName}")


class CustomTestRunner(unittest.TextTestRunner):
    resultclass = CustomTestResult


class TestLinkedList(unittest.TestCase):
    def test_reverse_list(self):
        """Пример с семинара 1->2->3->4"""
        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node4 = ListNode(4)
        node1.next = node2
        node2.next = node3
        node3.next = node4
        result = reverseList(node1)
        node4.next = node3
        node3.next = node2
        node2.next = node1
        node1.next = None
        self.assertEqual(result, node4)

    def test_two_elements(self):
        """Два элемента"""
        node1 = ListNode(1)
        node2 = ListNode(2)
        node1.next = node2
        result = reverseList(node1)
        node2.next = node1
        node1.next = None
        self.assertEqual(result, node2)

    def test_one_element(self):
        """Один элемент"""
        node1 = ListNode(1)
        result = reverseList(node1)
        self.assertEqual(result, node1)

    def test_empty_list(self):
        """Пустой список"""
        node = LinkedList()
        result = reverseList(node.head)
        self.assertEqual(result, None)


if __name__ == "__main__":
    runner = CustomTestRunner()
    unittest.main(testRunner=runner)
