from t_7 import merge_sorted_lists, ListNode
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


class TestMergeTwoLists(unittest.TestCase):
    def test_merge_sorted_lists(self):
        """Тест 1: Оба списка не пустые"""
        node_1_1 = ListNode(1)
        node_1_2 = ListNode(2)
        node_1_3 = ListNode(6)
        node_1_1.next = node_1_2
        node_1_2.next = node_1_3
        node_2_1 = ListNode(3)
        node_2_2 = ListNode(4)
        node_2_3 = ListNode(5)
        node_2_1.next = node_2_2
        node_2_2.next = node_2_3
        result = merge_sorted_lists(node_1_1, node_2_1)
        dummy = ListNode()
        cur = dummy
        cur.next = node_1_1
        node_1_1.next = node_1_2
        node_1_2.next = node_2_1
        node_2_1.next = node_2_2
        node_2_2.next = node_2_3
        node_2_3.next = node_1_3
        self.assertEqual(result, dummy.next)

    def test_first_list_is_empty(self):
        """Тест 2: Первый список пустой"""
        node_1_1 = ListNode()
        node_2_1 = ListNode(1)
        node_2_2 = ListNode(2)
        node_2_3 = ListNode(3)
        result = merge_sorted_lists(node_1_1, node_2_1)
        dummy = ListNode()
        cur = dummy
        cur.next = node_1_1
        node_1_1.next = node_2_1
        node_2_1.next = node_2_2
        node_2_2.next = node_2_3
        self.assertEqual(result, dummy.next)

    def test_second_list_is_empty(self):
        """Тест 3: Второй список пустой"""
        node_2_1 = ListNode()
        node_1_1 = ListNode(1)
        node_1_2 = ListNode(2)
        node_1_3 = ListNode(3)
        result = merge_sorted_lists(node_1_1, node_2_1)
        dummy = ListNode()
        cur = dummy
        cur.next = node_2_1
        node_2_1.next = node_1_1
        node_1_1.next = node_1_2
        node_1_2.next = node_1_3
        self.assertEqual(result, dummy.next)


if __name__ == "__main__":
    runner = CustomTestRunner()
    unittest.main(testRunner=runner)
