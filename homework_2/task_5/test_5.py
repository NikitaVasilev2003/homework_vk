from t_5_3 import isSubsequence
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


class TestIsSubsequence(unittest.TestCase):
    def test_is_subsequence(self):
        """Пример с семинара"""
        a = "abd"
        b = "uabqd"
        result = isSubsequence(a, b)
        self.assertTrue(result)

    def test_empty_first_string(self):
        """Первая строка пустая"""
        a = ""
        b = "uabqd"
        result = isSubsequence(a, b)
        self.assertTrue(result)

    def test_fail_test(self):
        """Вторая строка не содержит первую"""
        a = "x"
        b = "uabqd"
        result = isSubsequence(a, b)
        self.assertFalse(result)

    def test_second_shorter(self):
        """Вторая строка не содержит первую"""
        a = "dsfssfx"
        b = "dsfss"
        result = isSubsequence(a, b)
        self.assertFalse(result)


if __name__ == "__main__":
    runner = CustomTestRunner()
    unittest.main(testRunner=runner)
