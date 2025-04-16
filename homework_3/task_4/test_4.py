import unittest
from t_4_2 import extraLetter

# я не писал два файла для тестов, но назвал фунции одинаково, поэтому для текстирования
# другого случая достаточно написать
# from t_4_1 import extraLetter


class TestExtraLetter(unittest.TestCase):
    def test_first(self):
        """1 пример с семинара"""
        result = extraLetter("uio", "oeiu ")
        self.assertEqual("e", result)

    def test_second(self):
        """2 пример с семинара"""
        result = extraLetter("fe", "efo")
        self.assertEqual("o", result)

    def test_third(self):
        """3 пример с семинара"""
        result = extraLetter("ab", "ab")
        self.assertEqual("", result)

    def test_third(self):
        """4 пример с семинара"""
        result = extraLetter("bbb", "bbbb")
        self.assertEqual("b", result)

    def test_empty_string(self):
        """Первая пустая строка"""
        result = extraLetter("", "b")
        self.assertEqual("b", result)


if __name__ == "__main__":
    unittest.main()
