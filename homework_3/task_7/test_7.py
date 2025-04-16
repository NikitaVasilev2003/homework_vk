import unittest
from t_7_2 import groupAnagrams

# я не писал два файла для тестов, но назвал фунции одинаково, поэтому для текстирования
# другого случая достаточно написать
# from t_7_1 import groupAnagrams


class TestGroupAnagrams(unittest.TestCase):
    def test_first_case(self):
        """1 пример с семинара"""
        result = groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        s = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
        self.assertEqual(s, result)

    def test_second_case(self):
        """2 пример с семинара"""
        result = groupAnagrams(["won", "now", "aaa", "ooo", "ooo"])
        s = [["won", "now"], ["aaa"], ["ooo", "ooo"]]
        self.assertEqual(s, result)

    def test_negative_case(self):
        """В массиве пустая строка"""
        result = groupAnagrams([""])
        self.assertEqual([[""]], result)

    def test_two_identical_elements(self):
        """1 элемент"""
        result = groupAnagrams(["a"])
        self.assertEqual([["a"]], result)


if __name__ == "__main__":
    unittest.main()
