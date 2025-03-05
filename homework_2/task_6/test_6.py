from t_6_3 import isPalindrome
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


class TestIsPalindrome(unittest.TestCase):
    def test_is_palindrome(self):
        """Пример с семинара"""
        s = "abcba"
        result = isPalindrome(s)
        self.assertTrue(result)

    def test_empty_string(self):
        """Пустая строка"""
        s = ""
        result = isPalindrome(s)
        self.assertTrue(result)

    def test_fail(self):
        """Строка не полиндром"""
        s = "asefasfgfdgs"
        result = isPalindrome(s)
        self.assertFalse(result)

    def test_one_element(self):
        """Один элемент"""
        s = "a"
        result = isPalindrome(s)
        self.assertTrue(result)

    def test_two_elements(self):
        """Два элемента"""
        s = "ab"
        result = isPalindrome(s)
        self.assertFalse(result)


if __name__ == "__main__":
    runner = CustomTestRunner()
    unittest.main(testRunner=runner)
