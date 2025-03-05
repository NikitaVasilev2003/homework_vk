import unittest
from t_1_without_extra_memory import hasCycle, ListNode


class CustomTestResult(unittest.TextTestResult):
    def startTest(self, test):
        super().startTest(test)
        print(f"🚀 Запуск теста: {test._testMethodName} {test._testMethodDoc}")

    def addSuccess(self, test):
        super().addSuccess(test)
        print(f"✅ Тест пройден: {test._testMethodName}")

    def addFailure(self, test, err):
        super().addFailure(test, err)
        print(f"❌ Тест не пройден: {test._testMethodName}")

    def addError(self, test, err):
        super().addError(test, err)
        print(f"⚠️ Ошибка в тесте: {test._testMethodName}")


class CustomTestRunner(unittest.TextTestRunner):
    resultclass = CustomTestResult


class Cycle_List(unittest.TestCase):
    def test_cyclic_list(self):
        """Циклический список: 11->3->8->9->6->11->16->17->8"""
        node1 = ListNode(11)
        node2 = ListNode(3)
        node3 = ListNode(8)
        node4 = ListNode(9)
        node5 = ListNode(6)
        node6 = ListNode(11)
        node7 = ListNode(16)
        node8 = ListNode(17)
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5
        node5.next = node6
        node6.next = node7
        node7.next = node8
        node8.next = node3
        self.assertTrue(hasCycle(node1), msg="Неверная работа")

    def test_one_element(self):
        """Один элемент"""
        node1 = ListNode(1)
        node1.next = None
        self.assertFalse(hasCycle(node1))

    def test_cyclic_list_2(self):
        """Циклический список: 1 -> 2 -> 3 -> 1"""
        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node1.next = node2
        node2.next = node3
        node3.next = node1  # Замыкаем список
        self.assertTrue(
            hasCycle(node1), "Циклический список определен как нециклический"
        )

    def test_non_cyclic_list(self):
        """Нециклический список: 1 -> 2 -> 3"""
        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node1.next = node2
        node2.next = node3
        self.assertFalse(
            hasCycle(node1), "Нециклический список определен как циклический"
        )


if __name__ == "__main__":
    runner = CustomTestRunner()
    unittest.main(testRunner=runner)
