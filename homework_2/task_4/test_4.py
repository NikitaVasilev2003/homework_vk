import sys

sys.path.append("/Users/nikitavasilev/Desktop/вк_задачи_по_алгортмам")
from homework_2.node_1 import LinkedList

from t_4 import ListNode, removeElements
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


class TestRemoveElement(unittest.TestCase):
    def test_remove_element_1(self):
        """Пример с семинара"""
        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node4 = ListNode(4)
        node1.next = node2
        node2.next = node3
        node3.next = node4
        result = removeElements(node1, 3)
        node1.next = node2
        node2.next = node4
        self.assertEqual(result, node1)

    def test_remove_element_2(self):
        """Базовый пример с leetcode"""
        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(6)
        node4 = ListNode(3)
        node5 = ListNode(4)
        node6 = ListNode(5)
        node7 = ListNode(6)
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5
        node5.next = node6
        node6.next = node7
        result = removeElements(node1, 6)
        node1.next = node2
        node2.next = node4
        node4.next = node5
        node5.next = node6
        node6.next = None
        self.assertEqual(result, node1)

    def test_remove_all_elements(self):
        node1 = ListNode(7)
        node2 = ListNode(7)
        node3 = ListNode(7)
        node4 = ListNode(7)
        node1.next = node2
        node2.next = node3
        node3.next = node4
        result = removeElements(node1, 7)
        self.assertEqual(result, None)


if __name__ == "__main__":
    runner = CustomTestRunner()
    unittest.main(testRunner=runner)
