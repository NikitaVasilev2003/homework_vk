import sys

sys.path.append("/Users/nikitavasilev/Desktop/вк_задачи_по_алгортмам")
from homework_2.node_1 import LinkedList
from t_3 import ListNode, middleNode
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


class TestMiddleNode(unittest.TestCase):
    def test_odd_number(self):
        """Пример с семинара 3->8->9->6->11->16->17"""
        node1 = ListNode(3)
        node2 = ListNode(8)
        node3 = ListNode(9)
        node4 = ListNode(6)
        node5 = ListNode(11)
        node6 = ListNode(16)
        node7 = ListNode(17)
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5
        node5.next = node6
        node6.next = node7
        result = middleNode(node1)
        self.assertEqual(result, node4)

    def test_even_number(self):
        """Пример 3->8->9->6->11->16"""
        node1 = ListNode(3)
        node2 = ListNode(8)
        node3 = ListNode(9)
        node4 = ListNode(6)
        node5 = ListNode(11)
        node6 = ListNode(16)
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5
        node5.next = node6
        result = middleNode(node1)
        self.assertEqual(result, node4)

    def test_one_element(self):
        """Один элемент"""
        node1 = ListNode(1)
        result = middleNode(node1)
        self.assertEqual(result, node1)

    def test_two_elements(self):
        """Пара элементов"""
        node1 = ListNode(1)
        node2 = ListNode(2)
        node1.next = node2
        result = middleNode(node1)
        self.assertEqual(result, node2)

    def test_empty_list(self):
        """Пустой список"""
        node = LinkedList()
        result = middleNode(node.head)
        self.assertEqual(result, None)


if __name__ == "__main__":
    runner = CustomTestRunner()
    unittest.main(testRunner=runner)
